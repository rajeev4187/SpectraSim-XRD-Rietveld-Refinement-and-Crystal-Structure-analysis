# SpectraSim XRD — Rietveld refinement

**▶ Use it in your browser: https://spectrasim-xrd.streamlit.app/** — nothing to install.

Multiphase whole-pattern Rietveld refinement of powder X-ray diffraction
data: phase identification and quantification, lattice parameters,
crystallite size and microstrain, Le Bail decomposition, auto-indexing, and
an explicit statement of what the refinement does and does not support.

> **Citing this tool.** Kumar, R. (2026). *SpectraSim XRD — Rietveld
> refinement and phase analysis* [Computer software]. North Carolina Central
> University. https://github.com/rajeev4187/SpectraSim-XRD-Analyzer
> DOI: 10.5281/zenodo.TBD *(Zenodo archive — DOI pending)*.
> Machine-readable citation metadata: [`CITATION.cff`](CITATION.cff).

## Which workflow you need

Three routes, and the app decides between them rather than leaving it to you.

**1. You know the phases.** Load the pattern, set a background, add CIFs in
**Phases**, refine in **Refine**. Weight fractions, cells, size and strain
come out of **Results**.

**2. You do not know the phases.** **Phase ID** ranks candidates against your
own peaks and composes a multiphase answer automatically. Anything it
identifies has a published structure, so the route from there is refinement,
and the app says so and offers to carry the matches straight in.

**3. Nothing matches.** Phase ID tells you when nothing in the reference
corpus explains the pattern, and asks you to check the databases it cannot
query for you - COD, ICSD, Materials Project, ICDD PDF. It also offers the
*closest* structures it did find: a new material is usually a substituted or
distorted version of something already determined, and that parent can be
carried forward as a starting cell and space group rather than discarded for
not being an exact match. Only once you confirm the phase is unknown
everywhere does **Unknown Structure** become the route:
index the pattern to a cell, narrow the space group from the systematic
absences, extract intensities with no structural model, and solve for the
atoms *ab initio* by charge flipping. It refuses to be a shortcut - open it
for a pattern Phase ID already identified and it says so, because a solve
from powder data will be worse than the determination already published.

Solving is never the confirmation. Adding the solved structure back as an
ordinary phase and refining it is.

**Identification is useful even when you already have the CIFs.** A phase list
you assembled by hand explains the peaks you expected and says nothing about
the ones you did not, so Phase ID reports what your own phases leave over and
can search against those peaks alone - which is how a minor phase is found,
since it scores badly against the whole pattern by definition.

## What it does

- **Multiphase Rietveld refinement** with a Thompson-Cox-Hastings
  pseudo-Voigt profile, staged parameter release, and symmetry enforced
  rather than assumed - one displacement parameter and one occupancy per
  Wyckoff orbit, coordinates free only along site-symmetry-allowed
  directions, systematic absences removed group-theoretically.
- **Phase identification** scored two-sided, so a candidate must both explain
  your peaks and have its own strong lines present. Composes a multiphase
  answer by adding only phases that earn their place against what is still
  unexplained *and* against the whole pattern.
- **Le Bail decomposition and auto-indexing** for an unknown phase - a cell
  and profile constants without a structure. Two indexers: index assignment
  for the high-symmetry systems, and an ITO-style zone search reaching
  **monoclinic and triclinic**, which pins each cross term from an identity
  containing no unknowns rather than searching for it. Both refuse rather
  than guess: given peak lists from no lattice at all they return nothing.
  One button runs the whole analysis, ranks the candidate cells by parsimony
  rather than by fit - a doubled cell can always fit at least as well as the
  true one - and tells you when a cell dense enough to match anything has
  passed a test it could not fail.
- **Ab initio structure solution** from the pattern alone: a
  systematic-absence audit over all 230 groups and their settings, intensity
  extraction merged only by Friedel's law, charge flipping from several
  random starts, peak picking and element assignment, and a screen that
  refuses arrangements no chemistry can excuse.
- **Quantification** by Hill-Howard, with Brindley microabsorption and
  amorphous content from an internal standard reported beside it.
- **Crystallite size and microstrain** separated analytically, with the
  instrumental width measurable on a LaB6 or Si standard.
- **Instrument calibration** on LaB6 or Si - instrumental width, zero point
  and axial divergence, which can floor the sample widths so no phase is
  fitted narrower than the instrument itself.
- **Batch and series refinement** across a whole sample set, from uploads or
  a folder, with trends tracked. A batch refines every dataset against one
  shared phase list, or identifies each sample for itself from the same
  candidate pool - which is the difference between a series of one material
  and a set of different ones. Loaded singly, each sample keeps its own phase
  selection and its own fit.
- **Reads what your diffractometer wrote** - PANalytical XRDML, Bruker RAW,
  Excel, CSV and any two-column ASCII export, plus Origin projects (.opj,
  .opju) where Origin itself is installed, each worksheet that looks like a
  diffractogram becoming its own pattern.
- **Journal-ready output** - Rietveld plot with difference curve, phase
  fractions, structure drawing and series panel at 300 dpi, refined CIFs,
  R-factor and parameter tables, a methods paragraph and a consolidated
  report.

## What it will not claim

Every number carries the qualification it needs. That is the point of the
tool rather than a footnote to it.

- **Sizes are lower bounds and strains upper bounds** without an instrument
  standard measured on the same diffractometer. This is the commonest error
  in published crystallite sizes.
- **Microabsorption is reported, not applied** - the Brindley correction
  needs a particle radius you supply, so it is shown beside the uncorrected
  fractions rather than replacing them.
- **Weight fractions exclude amorphous content** unless an internal standard
  is used, and below about 1 wt% a phase is *detected*, not quantified.
- **A Le Bail R-factor is not a Rietveld R-factor** and the two are never
  compared.
- **Absences narrow a space group; they never select one.** Groups a powder
  pattern cannot tell apart are reported together as one answer rather than
  ranked against each other, and a reflection that is merely missing is not
  evidence that it is forbidden.
- **A solved structure is a hypothesis** until a refinement confirms it.
- **R factors answer different questions.** R_wp is the whole pattern and is
  dominated by whatever has the most intensity; R_Bragg is per phase and over
  integrated reflection intensities, so it is the one that judges the
  *structure*; and a Le Bail R_wp is neither, since its intensities were
  fitted rather than computed.


## Run it locally

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows;  source .venv/bin/activate on Unix
pip install -r requirements.txt
streamlit run SpectraSim-XRD.py
```

Python 3.12, 3.13 or 3.14. Sample data is in `release/Sample data`.

## How this repository is arranged

`SpectraSim-XRD.py` is a thin loader. The engine is
published as compiled bytecode in `release/web-demo`, one artifact per
supported Python version, because a `.pyc` is keyed to the exact interpreter
that produced it. The readable source is maintained privately; issues and
questions are welcome here.

Please include the pattern and the CIFs when reporting a refinement that goes
wrong - a Rietveld problem is rarely reproducible from a description.


## Acknowledgements

Built on [pymatgen](https://pymatgen.org) for structure handling, space-group
analysis and the X-ray scattering-factor tables (Ong *et al.*, *Comput.
Mater. Sci.* **68**, 314, 2013) and [spglib](https://spglib.readthedocs.io)
(Togo & Tanaka, arXiv:1808.01590); the forward-model kernel is validated
against pymatgen's own `XRDCalculator` to 1×10⁻¹³. Results were validated
against **FullProf** (Rodríguez-Carvajal, *Physica B* **192**, 55, 1993),
**GSAS-II** (Toby & Von Dreele, *J. Appl. Crystallogr.* **46**, 544, 2013)
and **HighScore Plus** (Degen *et al.*, *Powder Diffr.* **29**, S13, 2014).
Reference structures from the [Crystallography Open
Database](https://www.crystallography.net) and the [Materials
Project](https://materialsproject.org).

The 2026 correctness work took its arguments from published sources rather
than from taste, and some of the design is theirs. **XRDSol** (Yu, Zhu, Leng &
Zhu, *Nat. Commun.* 2026) is the reason a solved structure is screened for
plausibility at all: they used an independent energetic criterion to correct
39 ICSD entries that fitted their own patterns and had stood wrong for
decades. The interatomic-distance form of that screen is from **AXS** (Ling,
Montoya, Hung & Aykol, *Comput. Mater. Sci.* **214**, 111687, 2022).
[Ab-PXRD-Solver](https://github.com/MaterSim/Ab-PXRD-Solver) takes the
opposite approach to space groups and is why this app is explicit that
absences only ever narrow one; [ABINIT](https://github.com/abinit/abinit) is
the cautionary case on symmetry tolerances that argued for tying this app's
to a measured quantity.

## Licence

MIT — see `LICENSE`.
