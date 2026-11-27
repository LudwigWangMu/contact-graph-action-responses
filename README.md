# How Far Does a Push Travel? Paired Action Responses in Contact-Graph World Models

The experiments compare contact propagation, event-based predictions and learned corrections using paired initial states. The physical comparison uses endpoint poses from independently reset MIT MCube pushes.

## Manuscript authors

1. Yunjian Zhang — Shenzhen Kaihong Digital Industry Development Co., Ltd. [yunjzhang@xmu.edu.cn](mailto:yunjzhang@xmu.edu.cn) · [ORCID 0000-0002-0303-3671](https://orcid.org/0000-0002-0303-3671)
2. Ying Liu — Southern University of Science and Technology. [Liuy63@sustech.edu.cn](mailto:Liuy63@sustech.edu.cn) · [ORCID 0000-0001-6016-3184](https://orcid.org/0000-0001-6016-3184)
3. Aobo Li — Shenzhen Kaihong Digital Industry Development Co., Ltd. [ali09@qub.ac.uk](mailto:ali09@qub.ac.uk) · [ORCID 0009-0001-6868-9495](https://orcid.org/0009-0001-6868-9495)
4. Yilun Wu — Shenzhen Kaihong Digital Industry Development Co., Ltd. [wuyilun310@gmail.com](mailto:wuyilun310@gmail.com) · [ORCID 0000-0001-5169-4864](https://orcid.org/0000-0001-5169-4864)
5. Mu-Jiang-Shan Wang, Member, IEEE (corresponding author) — Shenzhen Kaihong Digital Industry Development Co., Ltd. and Harbin Institute of Technology. [wangmujiangshan-qy@kaihong.com](mailto:wangmujiangshan-qy@kaihong.com) and [wmjsdr0@gmail.com](mailto:wmjsdr0@gmail.com) · [ORCID 0000-0003-0950-4558](https://orcid.org/0000-0003-0950-4558)

## Verify the published results

Download and extract the [v1.0.1 release](https://github.com/LudwigWangMu/contact-graph-action-responses/releases/tag/v1.0.1), then run the following command in the extracted directory using Python 3.12. It checks the distributed file hashes and recomputes selected results from the archived observation-level records. The check runs offline with the Python standard library.

    python verify.py

For a full rerun, use a fresh working copy and follow the instructions below. After regenerating outputs, use `python verify.py --results-only` to check the numerical summaries.

## Run

From this directory, use Python 3.12 in a fresh environment.

```sh
python -m pip install -r requirements.txt
python reproduce.py
```

The complete run generates its simulation and uses the archived physical-endpoint measurements. It fits the learned baselines, evaluates both physics engines, and regenerates the numerical tables and vector plots. To run just the cross-engine test or the physical endpoint analysis, use `python code/branch_transfer.py` or `python code/real_reset_pairs.py`.

| Experiment | Archived evidence |
| --- | --- |
| Passive response, graph depth and action ranking | `data/scene_errors.csv`, `data/distance.csv`, `data/actions.csv` |
| Branched and packing configurations | `data/branch_pairs.csv` and `data/branch_summary.csv`. Rows at step 16 yield eight scene-paired comparisons in the root verifier. |
| Matched six-body layouts and hidden mass | `data/matched_geometry.csv`, `data/matched_geometry_summary.csv`, `data/mass_completion_pairs.csv` |
| Physical signed-command contrasts | `data/physical_reset_endpoints.csv` identifies 192 source records by member name and SHA-256. The paired contrasts use eight offsets and four independent repeats per signed condition. |

The simulation seeds are in the experiment drivers. Errors in the branch and physical contrast tables use millimetres. The physical endpoints were computed from the public repeatability archive of Peter K. T. Yu, Maria Bauza, Nima Fazeli and Alberto Rodriguez. To reconstruct them from the original records, run `python code/real_reset_pairs.py --fetch mcube-cache`. The per-member hash and exclusion list are supplied. [MCube data and acquisition protocol](https://mcube.mit.edu/push-dataset/)
