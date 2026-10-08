# Reference structures (CIF) for the CuWO4 / CuSe XRD phase assignment

Downloaded 7 August 2026 from the Crystallography Open Database (COD),
`https://www.crystallography.net/cod/<ID>.cif`. COD is open access and needs no
licence or API key. Every file below was checked after download: all 17 return
HTTP 200, parse as CIF, and contain a populated `_atom_site_fract_*` loop, so
each one can be used to compute a reference pattern.

The 90xxxxx and 901xxxx identifiers are the COD mirror of the American
Mineralogist Crystal Structure Database (AMCSD); the `_database_code_amcsd`
field in each file gives the AMCSD number if that citation is preferred.

Cell parameters quoted here were read from the downloaded files themselves, not
from the literature, so they describe exactly what is in this folder.

## Folder layout

Only the phases that actually produce reflections in the measured patterns are
kept at the top level. The other files are retained in subfolders rather than
deleted, since they document the exclusion arguments and the alternative cell
choices.

- top level, 7 files: phases identified in the samples
- `not-observed/`, 6 files: phases explicitly ruled out in the analysis
- `superseded/`, 4 files: entries measured under the wrong conditions, or
  chemically substituted, kept for reference only

## A note on wavelength

These files are crystal structures, not diffraction patterns. A CIF holds the
unit cell, the symmetry operations and the atomic coordinates, so a powder
pattern can be computed from any of them at any wavelength. Cu K-alpha is a
property of the calculation, not of the file, and there is therefore no such
thing as a "Cu K-alpha CIF" to select. The working notes computed their
reference patterns at Cu K-alpha1 = 1.54056 A, which is the value to reuse for
consistency.

Filtering these entries by the radiation used in the original measurement is not
possible in any case. COD records no `method` field for 15 of the 17 entries, and
only two carry any radiation information: COD 4000809 at Mo K-alpha, 0.71073 A,
and COD 4000806 at 0.45 A from a synchrotron source. Both of those are now in
`superseded/` or are single-crystal work. The 90xxxxx files inherited from AMCSD
contain no `_diffrn_radiation_*` fields whatsoever.

## Retained at top level: the phases that diffract

| File | Phase | Space group | Cell from CIF (A, deg) | Primary reference |
| --- | --- | --- | --- | --- |
| COD-4000809 | CuWO4 triclinic, ambient | P -1 | 4.708, 5.840, 4.884, 91.77, 92.47, 82.81 | Ruiz-Fuertes et al., Chem. Mater. 23, 4220 (2011) |
| COD-9014580 | CuO tenorite, 298 K | C 1 2/c 1 | 4.6837, 3.4226, 5.1288, beta 99.54 | Asbrink and Norrby, Acta Cryst. B 26, 8 (1970) |
| COD-9009856 | Cu3Se2 umangite | P -4 21 m | 6.4024, 6.4024, 4.2786 | Heyding and Murray, Can. J. Chem. 54, 841 (1976) |
| COD-9000063 | CuSe klockmannite | P 63/m m c | 3.938, 3.938, 17.25 | Berry, Am. Mineral. 39, 504 (1954) |
| COD-9009855 | Cu1.798Se berzelianite | F m -3 m | 5.765 | Heyding and Murray, Can. J. Chem. 54, 841 (1976) |
| COD-9015206 | Cu1.95Se berzelianite | F m -3 m | 5.787 | Yamamoto and Kashida, J. Solid State Chem. 93, 202 (1991) |
| COD-9008064 | Cu2Se berzelianite | F -4 3 m | 5.840 | Borchert, Z. Kristallogr. 106, 5 (1945) |

Three berzelianite entries are kept because the cubic Cu2-xSe stoichiometry is
still open. The notes refine a = 5.703 A, which lies below all three, so the set
brackets the composition rather than settling it.

## superseded/

| File | Phase | Why it is not used |
| --- | --- | --- |
| COD-4000806 | CuWO4, compressed | High-pressure structure, V = 128.3 against 133.06 A^3 ambient |
| COD-9005252 | Cu0.7Zn0.3WO4 cuproscheelite | 30 percent Zn on the Cu site, not the end member |
| COD-9016057 | CuO tenorite | Measured at 196 K, and deposited in the C 1 c 1 setting |
| COD-1008036 | CuWO4, neutron powder | Sound ambient alternative, superseded by 4000809 at R = 0.027 |

## not-observed/: phases explicitly ruled out in the analysis

| File | Phase | Space group | Cell from CIF (A, deg) |
| --- | --- | --- | --- |
| COD-9009854 | CuSe2 krutaite | P a -3 | 6.116 |
| COD-9007497 | Cu2O cuprite | P n -3 m | 4.2685 |
| COD-9007849 | Cu(OH)2 spertiniite | C m c 21 | 2.9471, 10.593, 5.2564 |
| COD-9001490 | CuSeO3.2H2O chalcomenite | P 21 21 21 | 6.674, 9.161, 7.398 |
| COD-5000216 | Cu metal, fcc | F m -3 m | 3.615 |
| COD-9011648 | Se trigonal, grey | P 31 2 1 | 4.368, 4.368, 4.958 |

Cu metal and trigonal Se were added here for completeness. The working notes
exclude both phases but did not list a COD entry for either, so these two files
are new rather than a re-download.

## Two corrections to the reference list in phase_assignment_notes.md

**1. Neither CuWO4 entry originally cited is a plain ambient CuWO4 structure.**

- COD 9005252 is *cuproscheelite*, `Cu0.7 Zn0.3 W O4`, from a Rietveld study of
  the sanmartinite to cuproscheelite solid solution (Redfern et al., Eur. J.
  Mineral. 7, 1019, 1995). It carries 30 percent Zn on the Cu site, so it is a
  substituted solid solution rather than the end member. Renamed accordingly.
- COD 4000806 comes from the high-pressure study of Ruiz-Fuertes et al. and has
  a = 4.620, b = 5.747, c = 4.857, gamma = 84.68 with V = 128.3 A^3, against
  133.06 A^3 for the same authors' ambient measurement. It is a compressed
  structure and will give reference peak positions shifted from an
  ambient-pressure laboratory pattern. Renamed to mark it as not for ambient use.

COD 4000809, from the same paper at ambient conditions, is a single-crystal
Mo K-alpha refinement with R = 0.027 and is the appropriate reference; it has
been added. COD 1008036, a neutron powder refinement, is included as a second
independent option.

The cell quoted as "literature" in the notes, a = 4.7026, b = 5.8389,
c = 4.8784 A with alpha = 91.677, beta = 92.469, gamma = 82.805 degrees, is that
of Kihlborg and Gebert, "CuWO4, a distorted Wolframite-type structure", Acta
Cryst. B 26, 1020 (1970), DOI 10.1107/S0567740870003515. That reference was
verified through Crossref. It is not held in COD as a pure CuWO4 entry, which is
why it does not correspond to any file in this folder. The calibration
conclusion in the notes is unaffected, since those literature values are correct
for ambient triclinic CuWO4, but the citation should point to Kihlborg and Gebert
rather than to a COD identifier.

**2. The CuO comparison used a 196 K structure.**

COD 9016057 is labelled `T = 196 K` in its own metadata, and its cell,
4.6893, 3.4268, 5.1321 A with beta = 99.653 degrees, is exactly the pair of
values quoted as "literature" in the notes. A room-temperature pattern should be
compared against the 298 K cell, 4.6837, 3.4226, 5.1288 A with
beta = 99.54 degrees (COD 9014580, Asbrink and Norrby 1970), which has been
added. The difference is roughly 0.1 percent in the cell edges and shifts
calculated 2theta by well under 0.05 degrees, so it does not change any phase
assignment, but the quoted comparison should use the 298 K figures.

Separately, COD 9016057 is deposited in the `C 1 c 1` setting rather than the
`C 2/c` given in the notes table. COD 9014580 uses `C 1 2/c 1`, which matches the
notes.

## Open item: the orthorhombic klockmannite distortion cannot be tested from COD

The notes attribute the anomalous intensity of the CuSe lines at 26.12, 41.04 and
47.33 degrees to the orthorhombic Cmcm distortion of room-temperature
klockmannite. That structure is not available here. A COD search on the formula
`Cu Se` returns eight entries and every one is the idealised hexagonal
P 63/m m c average structure: COD 9000063 plus the seven-member series
COD 2106764 to 2106770 from Milman's study, which are hexagonal at successively
smaller cells. A text search on "klockmannite" returns the same set. A Crossref
search did not return a citable primary reference for the orthorhombic structure
either.

Consequently the Cmcm explanation remains a hypothesis that has not been tested
against a real structure. To test it, the orthorhombic CIF has to come from ICSD
or from the supplementary material of the original structure paper, and the
reference must be verified before it is cited in the manuscript.

## Regenerating this folder

```bash
for id in 1008036 4000806 4000809 5000216 9000063 9001490 9005252 9007497 \
          9007849 9008064 9009854 9009855 9009856 9011648 9014580 9015206 9016057; do
  curl -sS -o "COD-${id}.cif" "https://www.crystallography.net/cod/${id}.cif"
done
```
