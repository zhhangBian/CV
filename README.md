# LaTeX CV

可维护的 XeLaTeX 中英文简历，推送到 `main` 后由 GitHub Actions 自动编译并发布。

## 文件结构

- [`cv.tex`](cv.tex) / [`cv_en.tex`](cv_en.tex)：中文 / 英文入口，只设置行距和章节标题样式
- [`resume-format.tex`](resume-format.tex)：共用模板，包含设计参数（颜色、间距、字号）和内容宏
- [`content/cv_zh.tex`](content/cv_zh.tex) / [`content/cv_en.tex`](content/cv_en.tex)：简历内容
- [`fonts/`](fonts)：随仓库分发的 Source Sans 3（SIL OFL），本地和 CI 编译结果一致；中文使用 Noto Sans CJK SC（思源黑体）
- [`assets/headshot.jpg`](assets/headshot.jpg)：证件照（当前未使用；需要时作为 `\Header` 的可选参数传入）

## 编译

```bash
./make.sh               # 同时编译中英文，输出到 build/
./make.sh cv_en.tex     # 只编译英文
```

依赖：`latexmk`、`texlive-xetex`、`texlive-lang-chinese`、`fonts-noto-cjk`（Debian/Ubuntu 包名）。

## 写内容：只用这些宏

| 宏 | 用途 |
| --- | --- |
| `\Header{姓名}{一句话定位}{\Contact{..}\Contact{..}}[照片]` | 页眉；联系方式之间的分隔符自动添加，换行时自动消失 |
| `\Section{标题}` | 章节 |
| `\Entry{标题}{右侧信息}` | 条目标题行；右侧为日期、作者身份或会议，宽度自适应 |
| `\Sub{文字}` | 条目下的灰色副标题（学位、课题组、方向） |
| `\Item{文字}` | 要点 |
| `\Pub{题目}{作者}{会议}{链接}` | 论文；用 `\Me{Zhuohang Bian}` 标出本人 |
| `\Skill{类别}{内容}` | 技能 |
| `\Award{名称}{年份}` | 荣誉，年份右对齐 |
| `\Links{\href{..}{[Paper]} ...}` | 不换行的链接组 |

约定：

- 内容文件中不写 `\vspace`、颜色或字号。需要调整视觉效果时，修改 `resume-format.tex` 顶部的 *Design tokens*，中英文会同步变化。
- 加粗只用于量化结果和关键技术名词，每条要点最多 1–2 处。
- 条目可以跨页，模板只保证标题后至少跟两行，不需要手动调整分页。

## 在线版本

- 中文版：<https://zhhangbian.github.io/CV/cv.pdf>
- English: <https://zhhangbian.github.io/CV/cv_en.pdf>
- 版本选择页：<https://zhhangbian.github.io/CV/>
