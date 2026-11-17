# GIT COMMIT LOG
**Course:** CSC10014 / Computational Thinking / 2026  
**Group ID:** Group 02  
**Domain:** Travel Planner Assistant  
**Repository:** Computational Thinking Project  
**Submission Milestone:** Project Proposal (Post-Presentation Phase)  
**Log Extraction Window:** Thursday, 15 October 2026 — Wednesday, 21 October 2026  

---

## 1. EXTRACTION COMMAND
```bash
git log --graph --all --stat --since="2026-10-15 00:00:00"
```

---

## 2. REPOSITORY COMMIT LOG (ALL BRANCHES)

```text
* commit 713a4d49e2afb2677e484fee5ee2c02893fd8887
| Author: CATO-OTAC <nba.cato.otac@gmail.com>
| Date:   Wed Oct 21 22:34:03 2026 +0700
| 
|     docs: complete post-presentation proposal deliverables and update engineering report
| 
|  docs/01_Engineering_Report/Engineering_Report.md  |   285 +-
|  docs/Group02_Report.md                            |   337 -
|  .../02_post/AI_Usage_Declaration.md               |    95 +
|  .../02_post/AI_Usage_Declaration.pdf              |   Bin 0 -> 383421 bytes
|  .../02_post/Group02_Presentation.pdf              | 75844 ++++++++++++++++++
|  .../02_post/Group02_Report.html                   |   901 +
|  .../02_post/Group02_Report.md                     |   586 +
|  .../02_post/Group02_Report.pdf                    |   Bin 0 -> 681798 bytes
|  .../02_post/Task_Distribution.md                  |    55 +
|  .../02_post/Task_Distribution.pdf                 |   Bin 0 -> 282101 bytes
|  10 files changed, 77753 insertions(+), 350 deletions(-)
|   
*   commit 8a6f597171eb84896f6bda7238eef030a196b427
|\  Merge: 086f549 80df5f1
| | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | Date:   Wed Oct 21 21:58:10 2026 +0700
| | 
| |     Merge remote-tracking branch 'origin/25127022_Chau' into dev and resolve conflicts
| | 
| * commit 80df5f1260258e376efe6c531eb25caa35a49320
| | Author: HwC <165186725+HwangChou@users.noreply.github.com>
| | Date:   Wed Oct 21 20:20:05 2026 +0700
| | 
| |     Add files via upload
| | 
| |  xacdinhvande, huonggiaiquyet (post_present).md | 336 +++++++++++++++++++++
| |  1 file changed, 336 insertions(+)
| | 
| * commit 02d4d1596411b1a3ba5924d1b475d3e6b505682a
| | Author: HwC <165186725+HwangChou@users.noreply.github.com>
| | Date:   Mon Oct 19 20:43:59 2026 +0700
| | 
| |     Add files via upload
| | 
| |  AI Usage Declaration.md | 38 ++++++++++++++++++++++++++++++++++++++
| |  1 file changed, 38 insertions(+)
| |   
* |   commit 086f5497c5a42a066849eae3847ab8107d044e6a
|\ \  Merge: da45be0 253d756
| | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | Date:   Wed Oct 21 21:42:39 2026 +0700
| | | 
| | |     Merge remote-tracking branch 'origin/nhu' into dev
| | | 
| * | commit 253d75622c209e42fd34022c7a7f831b281a77a6
| | | Author: nhknhu2509-eng <nhknhu2509@clc.fitus.edu.vn>
| | | Date:   Wed Oct 21 20:41:43 2026 +0700
| | | 
| | |     Addcontentdataset
| | | 
| | |  adddataset.md | 76 +++++++++++++++++++++++++++++++++++++++++++++++++++++
| | |  1 file changed, 76 insertions(+)
| | | 
| * | commit 101ad6e53ca7db592c6d4b6da2f3b833d3d4b8cc
| | | Author: nhknhu2509-eng <nhknhu2509@clc.fitus.edu.vn>
| | | Date:   Mon Oct 19 19:52:40 2026 +0700
| | | 
| | |     Add AI usage declaration
| | | 
| | |  AI Usage Declaration.md | 38 ++++++++++++++++++++++++++++++++++++++
| | |  1 file changed, 38 insertions(+)
| | |   
* | |   commit da45be0b142d1d5cc959c5db9447ed623f7da869
|\ \ \  Merge: 6e57b6f 7c57045
| | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | Date:   Wed Oct 21 21:37:48 2026 +0700
| | | | 
| | | |     Merge branch 'algorithm_design_and_abstraction' into dev
| | | | 
| * | | commit 7c57045c82c3bddbaa078c421684dc6a21a206db
| | | | Author: tntthien <tntthien2535@clc.fitus.edu.vn>
| | | | Date:   Wed Oct 21 17:14:15 2026 +0700
| | | | 
| | | |     update from line 65 to line 71
| | | | 
| | | |  docs/Group02_Report.md | 337 +++++++++++++++++++++++++++++++++++++++++
| | | |  1 file changed, 337 insertions(+)
| | | | 
| * | | commit 43180f662344ecb66582f4677836c250a3ac64e1
| | | | Author: tntthien <tntthien2535@clc.fitus.edu.vn>
| | | | Date:   Mon Oct 19 19:03:25 2026 +0700
| | | | 
| | | |     UPLOAD FILE PDF
| | | | 
| | | |  .../algorithm_design_and_abstraction.pdf        | Bin 0 -> 66091 bytes
| | | |  1 file changed, 0 insertions(+), 0 deletions(-)
| | | |   
* | | |   commit 6e57b6fd22f55f893915d14029a333b048027e9d
|\ \ \ \  Merge: be6f2da 15b30e2
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Wed Oct 21 21:31:16 2026 +0700
| | | | | 
| | | | |     Merge branch 'dev' of https://github.com/CATO-OTAC/Computation-Thinking into dev
| | | | |   
| * | | |   commit 15b30e29baa46fbc7038eca53e8ad5dac1a530a5
| |\ \ \ \  Merge: 7eb8b98 98052ab
| | | | | | Author: Nguyễn Bình An <nba.cato.otac@gmail.com>
| | | | | | Date:   Tue Oct 20 10:14:01 2026 +0700
| | | | | | 
| | | | | |     Merge pull request #3 from CATO-OTAC/An
| | | | | |     
| | | | | |     An
| | | | | |   
* | | | | |   commit be6f2daa7fcdc7f0605c9905bece5dc4f78f0b8d
|\ \ \ \ \ \  Merge: 7eb8b98 98052ab
| |/ / / / /  Author: CATO-OTAC <nba.cato.otac@gmail.com>
|/| / / / /   Date:   Tue Oct 20 10:12:10 2026 +0700
| |/ / / /    
| | | | |         Merge branch 'An' into dev
| | | | | 
| * | | | commit 98052ab24a0fd85ef3f85104f92d819b829c2dbf
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Tue Oct 20 09:40:52 2026 +0700
| | | | | 
| | | | |     sync engineering report, architecture design, and team logbook
| | | | | 
| | | | |  .../Engineering_Report.md                    | 186 ++++++++---------
| | | | |  .../abstraction_algorithmdesign.md           |  99 ++++-----
| | | | |  docs/07_Team_Logbook/AI_Usage_Record.md      |  14 +-
| | | | |  docs/07_Team_Logbook/Contribution_Summary.md |   4 +-
| | | | |  4 files changed, 147 insertions(+), 156 deletions(-)
| | | | | 
| * | | | commit d5aae8c4fd4c16dbcd95c5420d4fccd248482163
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Tue Oct 20 09:40:19 2026 +0700
| | | | | 
| | | | |     reorganize proposal deliverables into 02 directory and cleanup root files
| | | | | 
| | | | |  Noidung_Xacdinhvande_Huonggiaiquyet.docx     | Bin 21490 -> 0 bytes
| | | | |  Xacdinhvande-Huonggiaiquyet.pptx             | Bin 4478220 -> 0 bytes
| | | | |  fix_xdvd,hgq.pptx                            | Bin 6949550 -> 0 bytes
| | | | |  .../02}/AI_Usage_Declaration.md              |  14 +-
| | | | |  .../02}/AI_Usage_Declaration.pdf             | Bin 306882 -> 298177 bytes
| | | | |  .../02}/Git_Commit_Log.md                    |   0
| | | | |  .../02}/Git_Commit_Log.pdf                   | Bin 145284 -> 134862 bytes
| | | | |  .../02}/Group02_Presentation.pdf             |   0
| | | | |  .../02/Group02_Report.html                   | 527 +++++++++++++++++
| | | | |  .../02}/Group02_Report.md                    | 186 +++---
| | | | |  .../02}/Group02_Report.pdf                   | Bin 438283 -> 432096 bytes
| | | | |  .../02}/Task_Distribution.md                 |   2 +-
| | | | |  .../02}/Task_Distribution.pdf                | Bin 155514 -> 176236 bytes
| | | | |  xac dinh van de, huong giai quyet.pptx       | Bin 6949550 -> 0 bytes
| | | | |  14 files changed, 629 insertions(+), 100 deletions(-)
| | | | | 
| * | | | commit ee8484afe45da03781675d0be20b02af12e85aaf
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Tue Oct 20 09:37:39 2026 +0700
| | | | | 
| | | | |     docs: add project structure guide and update gitignore
| | | | | 
| | | | |  .gitignore        |  87 +++++++++++++++++++++++++++++++++++
| | | | |  GIT_SYNC_GUIDE.md |  89 ++++++++++++++++++++++++++++++++++++
| | | | |  PROJECT_GUIDE.md  | 108 ++++++++++++++++++++++++++++++++++++++++++++
| | | | |  PROJECT_GUIDE.pdf | Bin 0 -> 376563 bytes
| | | | |  4 files changed, 284 insertions(+)
| | | | | 
* | | | | commit 7eb8b98f3eb5ccd3e65bf146b47ab6c91365bd17
|\| | | | Merge: 9b270f6 5cec275
| | | | | Author: Nguyễn Bình An <nba.cato.otac@gmail.com>
| | | | | Date:   Mon Oct 19 21:35:21 2026 +0700
| | | | | 
| | | | |     Merge pull request #2 from CATO-OTAC/An
| | | | |     
| | | | |     An
| | | | | 
| * | | | commit 5cec275b67dfd96587a21219a4d68c8ab8a5810a
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Mon Oct 19 21:24:36 2026 +0700
| | | | | 
| | | | |     update git commit log using teacher command
| | | | | 
| | | | |  .../Group02/Git_Commit_Log.md                | 358 +++++++++++++++--
| | | | |  .../Group02/Git_Commit_Log.pdf               | Bin 175254 -> 145284 bytes
| | | | |  2 files changed, 324 insertions(+), 34 deletions(-)
| | | | | 
| * | | | commit 7191943a65562df17c2cb53aaf63235f4f1c6e7e
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Mon Oct 19 21:20:21 2026 +0700
| | | | | 
| | | | |     update git commit log with recent commits
| | | | | 
| | | | |  .../Group02/Git_Commit_Log.md                |  52 ++++++++++-------
| | | | |  .../Group02/Git_Commit_Log.pdf               | Bin 176860 -> 175254 bytes
| | | | |  2 files changed, 31 insertions(+), 21 deletions(-)
| | | | | 
| * | | | commit 3143a0462e1bd719bdd6c09450b5c101f81d3b47
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Mon Oct 19 21:19:58 2026 +0700
| | | | | 
| | | | |     add weekly proposal submission files
| | | | | 
| | | | |  .../Group02/AI_Usage_Declaration.md          |    73 +
| | | | |  .../Group02/AI_Usage_Declaration.pdf         |   Bin 0 -> 306882 bytes
| | | | |  .../Group02/Git_Commit_Log.md                |    33 +
| | | | |  .../Group02/Git_Commit_Log.pdf               |   Bin 0 -> 176860 bytes
| | | | |  .../Group02/Group02_Presentation.pdf         | 54194 +++++++++++++++
| | | | |  .../Group02/Group02_Report.md                |   329 +
| | | | |  .../Group02/Group02_Report.pdf               |   Bin 0 -> 438283 bytes
| | | | |  .../Group02/Task_Distribution.md             |    22 +
| | | | |  .../Group02/Task_Distribution.pdf            |   Bin 0 -> 155514 bytes
| | | | |  9 files changed, 54651 insertions(+)
| | | | | 
| * | | | commit ccf97e214e33ec4cecafb97e3d961692ac952350
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Mon Oct 19 21:19:48 2026 +0700
| | | | | 
| | | | |     add group presentation pdf
| | | | | 
| | | | |  Group02_Presentation.pdf | 54194 +++++++++++++++++++++++++++++++++++
| | | | |  1 file changed, 54194 insertions(+)
| | | | | 
| * | | | commit c8054ccb9b6e33897177cb044642202edfd63f3f
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Mon Oct 19 21:19:39 2026 +0700
| | | | | 
| | | | |     update contribution summary and task distribution
| | | | | 
| | | | |  docs/07_Team_Logbook/Contribution_Summary.md | 39 ++++++++++++++++++
| | | | |  1 file changed, 39 insertions(+)
| | | | | 
| * | | | commit b33c8d22a4260ab22b05799ccc10ce4d0922fdbc
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Mon Oct 19 21:19:27 2026 +0700
| | | | | 
| | | | |     update AI usage record
| | | | | 
| | | | |  docs/07_Team_Logbook/AI_Usage_Record.md | 73 +++++++++++++++++++++++
| | | | |  1 file changed, 73 insertions(+)
| | | | | 
| * | | | commit 5b85364bf7d2dc661ce0a25869d5f2654c4b10c6
| | | | | Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | | | | Date:   Mon Oct 19 21:19:18 2026 +0700
| | | | | 
| | | | |     update engineering report w1
| | | | | 
| | | | |  .../Engineering_Report.md                    | 300 ++++++++++++++++-
| | | | |  1 file changed, 284 insertions(+), 16 deletions(-)
| | | | |   
| * | | |   commit f804a997e0d12094da309d58ade60e189e25b892
| |\ \ \ \  Merge: eedbb6b 63519c3
| | | |_|/  Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | |/| |   Date:   Mon Oct 19 17:19:18 2026 +0700
| | | | |   
| | | | |       Merge branch '25127022_nthchau' into An
| | | | | 
| | * | | commit 63519c3f7f59fae81921ae5134a4c3ad26366f1c
| | | | | Author: HwC <165186725+HwangChou@users.noreply.github.com>
| | | | | Date:   Mon Oct 19 16:22:48 2026 +0700
| | | | | 
| | | | |     Add files via upload
| | | | | 
| | | | |  xac dinh van de, huong giai quyet.pptx | Bin 0 -> 6949550 bytes
| | | | |  1 file changed, 0 insertions(+), 0 deletions(-)
| | | | | 
| | * | | commit 8a7ee71baaf20e809ee10ed76aca55ac489af371
| | | | | Author: HwC <165186725+HwangChou@users.noreply.github.com>
| | | | | Date:   Mon Oct 19 16:22:24 2026 +0700
| | | | | 
| | | | |     Add files via upload
| | | | | 
| | | | |  xac dinh van de, huong giai quyet.md | 160 +++++++++++++++++++++++++
| | | | |  1 file changed, 160 insertions(+)
| | | | |   
| * | | |   commit eedbb6b4d8d3e732b3a0647edc24f9c470a4627c
| |\ \ \ \  Merge: 5f0dc2c 8e0a9ae
| | | |_|/  Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | |/| |   Date:   Mon Oct 19 17:13:55 2026 +0700
| | | | |   
| | | | |       Merge branch '25127222_Nhu' into An
| | | | | 
| | * | | commit 8e0a9ae139d826aee55da610a7a0f9db338ddb8a
| | | | | Author: nhknhu2509-eng <nhknhu2509@clc.fitus.edu.vn>
| | | | | Date:   Mon Oct 19 16:21:07 2026 +0700
| | | | | 
| | | | |     fix report w1
| | | | | 
| | | | |  report_xdvd,hgq.md | 160 +++++++++++++++++++++++++++++++++++++++++++
| | | | |  1 file changed, 160 insertions(+)
| | | | | 
| | * | | commit 5f1330938912a9f7fb0fb6603487adac13dd583e
| | | | | Author: nhknhu2509-eng <nhknhu2509@clc.fitus.edu.vn>
| | | | | Date:   Mon Oct 19 15:58:38 2026 +0700
| | | | | 
| | | | |     fix ppt w1
| | | | | 
| | | | |  fix_xdvd,hgq.pptx | Bin 0 -> 6949550 bytes
| | | | |  1 file changed, 0 insertions(+), 0 deletions(-)
| | | | | 
| | * | | commit 79c51f5b4cb9f8e0ee8f838b3291e10320f50542
| | | | | Author: nhknhu2509-eng <nhknhu2509@clc.fitus.edu.vn>
| | | | | Date:   Mon Oct 19 14:57:10 2026 +0700
| | | | | 
| | | | |     Add content w1
| | | | | 
| | | | |  Noidung_Xacdinhvande_Huonggiaiquyet.docx | Bin 0 -> 21490 bytes
| | | | |  1 file changed, 0 insertions(+), 0 deletions(-)
| | | | | 
| | * | | commit da1b8973a8807845d5b65e4301819a434f266c44
| | |/ /  Author: nhknhu2509-eng <nhknhu2509@clc.fitus.edu.vn>
| | | |   Date:   Mon Oct 19 14:50:08 2026 +0700
| | | |   
| | | |       Add files via upload
| | | |       
| | | |       Add slide w1
| | | |   
| | | |    Xacdinhvande-Huonggiaiquyet.pptx | Bin 0 -> 4478220 bytes
| | | |    1 file changed, 0 insertions(+), 0 deletions(-)
| | | |   
| * | |   commit 5f0dc2c655e7cd19e3ff53496b218d23efe4daf5
| |\ \ \  Merge: db52498 a52321f
| | | |/  Author: CATO-OTAC <nba.cato.otac@gmail.com>
| | |/|   Date:   Mon Oct 19 16:49:01 2026 +0700
| | | |   
| | | |       Merge branch 'algorithm_design_and_abstraction' into An
| | | | 
| | * | commit a52321f7e3350fc28a3e5ff12dc5933f0bf69622
| | | | Author: tntthien <tntthien2535@clc.fitus.edu.vn>
| | | | Date:   Mon Oct 19 14:27:57 2026 +0700
| | | | 
| | | |     Upload AI Usage
| | | | 
| | | |  docs/03_Architecture_Design/Readme.md | 0
| | | |  1 file changed, 0 insertions(+), 0 deletions(-)
| | | | 
| | * | commit ea9581b6de7e9578fd8957ad919d9151d1e6729e
| | |/  Author: tntthien <tntthien2535@clc.fitus.edu.vn>
| | |   Date:   Mon Oct 19 14:26:58 2026 +0700
| | |   
| | |       Add files via upload
| | |   
| | |    .../abstraction_algorithmdesign.md            | 55 +++++++++++++++++++
| | |    1 file changed, 55 insertions(+)
| | | 
* | | commit 9b270f6b13b93082205d34f3da412b455bad72d1
|\| | Merge: f456b72 db52498
| |/  Author: Nguyễn Bình An <nba.cato.otac@gmail.com>
|/|   Date:   Mon Oct 19 15:10:48 2026 +0700
| |   
| |       Merge pull request #1 from CATO-OTAC/An
| |       
| |       add group info to README and initialize engineering report template
| | 
| * commit db52498165e23a3178781c46fadb1390729b044d
|/  Author: CATO-OTAC <nba.cato.otac@gmail.com>
|   Date:   Mon Oct 19 15:02:02 2026 +0700
|   
|       add group info to README and initialize engineering report template
|   
|    README.md                                        | 14 +++++
|    docs/01_Engineering_Report/Engineering_Report.md | 61 ++++++++++++++++++++
|    2 files changed, 75 insertions(+)
 \ 
  * commit f456b7226199c462e320a8cffdf81a7e1fdf55b1
    Author: CATO-OTAC <nba.cato.otac@gmail.com>
    Date:   Mon Oct 19 00:27:32 2026 +0700
    
        setup initial folder structure
    
     .env.example                                       | 0
     .github/pull_request_template.md                   | 0
     .gitignore                                         | 0
     README.md                                          | 1 +
     docs/01_Engineering_Report/Engineering_Report.md   | 0
     docs/03_Architecture_Design/interface_contracts.md | 0
     docs/03_Architecture_Design/pseudocode.md          | 0
     docs/04_Evaluation_Pack/benchmark_test_set.json    | 0
     docs/04_Evaluation_Pack/error_taxonomy.md          | 0
     docs/04_Evaluation_Pack/improvement_evidence.md    | 0
     docs/04_Evaluation_Pack/metrics_results.md         | 0
     docs/05_Failure_Risk_Pack/failure_catalogue.md     | 0
     docs/05_Failure_Risk_Pack/privacy_safeguards.md    | 0
     docs/07_Team_Logbook/AI_Usage_Record.md            | 0
     docs/07_Team_Logbook/Contribution_Summary.md       | 0
     src/backend/main.py                                | 0
     src/backend/requirements.txt                       | 0
     17 files changed, 1 insertion(+)
  
* commit 9f3d4256110d2ab3aa35abd8a9c852bdff45ca26
| Author: Nguyễn Bạch Thành Nhân <nhantino1234@gmail.com>
| Date:   Wed Oct 21 22:09:27 2026 +0700
| 
|     UPDATE
| 
|  25127111_W01_05/Git Commit Log.md  |    59 +
|  25127111_W01_05/README.md          |     2 +-
|  PRE_presentation.zip               |   Bin 0 -> 4661400 bytes
|  post_presentation/README-261021.md |    66 +
|  post_presentation/report (5).pdf   |   Bin 0 -> 2115702 bytes
|  post_presentation/report.md        |   360 +
|  post_presentation/slides.pdf       | 76223 +++++++++++++++++++++++++++++++++
|  7 files changed, 76709 insertions(+), 1 deletion(-)
| 
* commit e86d309ecaf135bba21d746f59af0970d576422f
| Author: Nguyễn Bạch Thành Nhân <nhantino1234@gmail.com>
| Date:   Mon Oct 19 19:21:46 2026 +0700
| 
|     fix_prepresentation
| 
|  25127111_W01_05/README.md                              | 2 +-
|  25127111_W01_05/Git Commit Log.md => Git Commit Log.md | 0
|  2 files changed, 1 insertion(+), 1 deletion(-)
| 
* commit 3b111c09a7930804cf75b6169de973c20cc6278c
| Author: Nguyễn Bạch Thành Nhân <nhantino1234@gmail.com>
| Date:   Mon Oct 19 19:08:56 2026 +0700
| 
|     prepresentation
| 
|  25127111_W01_05/Git Commit Log.md            |  10 ++++++
|  25127111_W01_05/README.md                    |   2 +-
|  PRE_presentation/Pre_Presentation-261019.md  |  43 +++++++++++++++++++++++++
|  PRE_presentation/Pre_Presentation-261019.pdf | Bin 0 -> 473385 bytes
|  PRE_presentation/Pre_presentation_slides.pdf | Bin 0 -> 4237370 bytes
|  PRE_presentation/Readme.md                   |  27 ++++++++++++++++
|  6 files changed, 81 insertions(+), 1 deletion(-)
| 
* commit d7aa66883d45f1e43ce089a0db42dc6f68a6cfa8
| Author: Nguyễn Bạch Thành Nhân <nhantino1234@gmail.com>
| Date:   Fri Oct 16 21:35:32 2026 +0700
| 
|     lab01_update
| 
|  25127111_W01_05/Git Commit Log.md | 49 +++++++++++++++++++++++++++++++++++++
|  25127111_W01_05/README.md         | 45 ++++++++++++++++++++++++++++++++++
|  2 files changed, 94 insertions(+)
| 
* commit f24175a99b634c8b4117d97239b6db220dc7b650
| Author: Nguyễn Bạch Thành Nhân <nhantino1234@gmail.com>
| Date:   Fri Oct 16 20:55:11 2026 +0700
| 
|     W1
| 
|  25127111_W01_02/25127111_W01_02.md        | 265 ----------------------------
|  25127111_W01_02/25127111_W01_02.pdf       | Bin 218084 -> 0 bytes
|  25127111_W01_05/Exercise01/Exercise01.md  |  15 ++
|  25127111_W01_05/Exercise01/Exercise01.pdf | Bin 0 -> 106759 bytes
|  25127111_W01_05/Exercise02/Exercise02.md  | 123 +++++++++++++
|  25127111_W01_05/Exercise02/Exercise02.pdf | Bin 0 -> 1551781 bytes
|  25127111_W01_05/Exercise03/Exercise03.md  |  69 ++++++++
|  25127111_W01_05/Exercise03/Exercise03.pdf | Bin 0 -> 1285706 bytes
|  25127111_W01_05/Exercise04/Exercise04.md  |  22 +++
|  25127111_W01_05/Exercise04/Exercise04.pdf | Bin 0 -> 157219 bytes
|  25127111_W01_05/Exercise05/Exercise05.md  |  50 ++++++
|  25127111_W01_05/Exercise05/Exercise05.pdf | Bin 0 -> 886075 bytes
|  12 files changed, 279 insertions(+), 265 deletions(-)
| 
* commit e9a0bc9963c8c8a489d9ca4dcbc3587f4e49c2b3
| Author: Nguyễn Bạch Thành Nhân <nhantino1234@gmail.com>
| Date:   Thu Oct 15 22:38:15 2026 +0700
| 
|     w01
| 
|  25127111_W01_02.zip                 | Bin 130534 -> 0 bytes
|  25127111_W01_02/25127111_W01_02.md  | 265 ++++++++++++++++++++++++++++++++++
|  25127111_W01_02/25127111_W01_02.pdf | Bin 0 -> 218084 bytes
|  3 files changed, 265 insertions(+)
| 
* commit a79999db3c766838fe20c824b989b9259f56eae4
| Author: Nguyễn Bạch Thành Nhân <nhantino1234@gmail.com>
| Date:   Thu Oct 15 22:36:49 2026 +0700
| 
|     Create 25127111_W01_02.zip
| 
|  25127111_W01_02.zip | Bin 0 -> 130534 bytes
|  1 file changed, 0 insertions(+), 0 deletions(-)
| 
* commit f90511b3f936ad4fb10cefc561d72b74c93232e1
  Author: Nguyễn Bạch Thành Nhân <nhantino1234@gmail.com>
  Date:   Thu Oct 15 21:25:42 2026 +0700
  
      Initial commit
  
   .gitattributes | 2 ++
   README.md      | 2 ++
   2 files changed, 4 insertions(+)

```
