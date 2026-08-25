"""SpectraSim XRD — Rietveld refinement and Crystal Structure
Analysis.

Streamlit entry point.

Deploy on Streamlit Community Cloud with this file as the main file path.
Run locally with:

    streamlit run SpectraSim-XRD.py

This is the only source file in the repository. The refinement engine is
published as compiled Python bytecode in version-suffixed files under
``release/web-demo``:

    xrd_engine.cp312.pyc   <- for Python 3.12
    xrd_engine.cp313.pyc   <- for Python 3.13 (Streamlit Cloud default)
    xrd_engine.cp314.pyc   <- for Python 3.14
    xrd_engine.cpXY.pyc    <- generally, ".cp" + major + minor

The loader picks the .pyc matching the running Python and exec()s its bytecode
in this module's global scope, so ``streamlit run`` behaves exactly as if the
engine source were written here.

Why one file per version? A .pyc is keyed to the exact interpreter version
through its magic number, so a build for 3.12 will not load on 3.14 and vice
versa. Streamlit Cloud pins a Python version while local testing runs on
whatever is in the dev venv — shipping one .pyc per target is the simplest way
both paths work without publishing the source.

Maintainers: regenerate the artifacts from the private upstream sources with
``tools/build_web_engine.py`` in the upstream XRD folder
(``py -3.13 tools/build_web_engine.py``, or ``--all`` for every target).
"""
from __future__ import annotations

import marshal
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ENGINE_DIR = os.path.join(_HERE, "release", "web-demo")
_STEM = "xrd_engine"


def _verify_under_streamlit_run() -> None:
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
    except ImportError:
        sys.stderr.write(
            "\n[SpectraSim-XRD] Streamlit is not installed in this Python.\n"
            "  Install it first:    pip install -r requirements.txt\n"
            "  Then launch with:    streamlit run "
            + os.path.basename(__file__) + "\n\n"
        )
        sys.exit(1)
    if get_script_run_ctx() is None:
        sys.stderr.write(
            "\n[SpectraSim-XRD] This script must be launched with "
            "`streamlit run`, not plain `python`.\n\n"
            "  WRONG:  python " + os.path.basename(__file__) + "\n"
            "  RIGHT:  streamlit run " + os.path.basename(__file__) + "\n\n"
            "Reason: the engine calls st.set_page_config / st.sidebar at "
            "module load\ntime, which need Streamlit's per-thread "
            "ScriptRunContext. That context is\nonly set up by "
            "`streamlit run`.\n\n"
        )
        sys.exit(1)


def _available_versions() -> list[str]:
    """Python-version tags for every engine .pyc in this deployment."""
    tags = []
    for name in os.listdir(_ENGINE_DIR):
        if name.startswith(_STEM + ".cp") and name.endswith(".pyc"):
            tags.append(name[len(_STEM) + 1:-len(".pyc")])
    return sorted(tags)


def _load_engine_code():
    py_tag = f"cp{sys.version_info.major}{sys.version_info.minor}"
    pyc = os.path.join(_ENGINE_DIR, f"{_STEM}.{py_tag}.pyc")

    if not os.path.isfile(pyc):
        shipped = ", ".join(_available_versions()) or "none"
        raise FileNotFoundError(
            f"No engine bytecode for Python {sys.version_info.major}."
            f"{sys.version_info.minor} (looked for {_STEM}.{py_tag}"
            f".pyc). This deployment ships .pyc for: {shipped}. Either run "
            f"with one of those Python versions, or rebuild for "
            f"{sys.version_info.major}.{sys.version_info.minor} with "
            f"tools/build_web_engine.py in the upstream XRD folder."
        )

    # A Python >=3.7 .pyc header is 16 bytes: 4-byte magic, 4-byte flags and
    # 8 bytes of source hash or mtime+size. The rest is the marshalled code.
    with open(pyc, "rb") as fh:
        blob = fh.read()
    try:
        return marshal.loads(blob[16:])
    except Exception as exc:
        raise RuntimeError(
            f"Failed to load {os.path.basename(pyc)}. The file is named for "
            f"Python {py_tag} but its bytecode header did not validate — "
            f"most likely it was built by a different interpreter and renamed "
            f"by hand. Rebuild it with the matching Python."
        ) from exc


_verify_under_streamlit_run()
exec(_load_engine_code(), globals())

# A sidebar copy of the citation. The engine renders its own in the main
# area from a string baked into the bytecode, so changing what the app shows
# there means editing the engine source and rebuilding the .pyc — editing
# this caption alone will not do it.
import streamlit as _st

_st.sidebar.markdown("---")
_st.sidebar.caption(
    "**Cite this tool:** Kumar, R. (2026). *SpectraSim XRD — Rietveld "
    "refinement and Crystal Structure Analysis* [Computer software]. North "
    "Carolina Central University. "
    "https://github.com/rajeev4187/SpectraSim-XRD-Rietveld-Refinement-and-Crystal-Structure-analysis. "
    "DOI: 10.5281/zenodo.22088389"
)
