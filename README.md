# LaTeX CV

这个仓库保存可维护的 XeLaTeX 中英文简历，并通过 GitHub Actions 自动编译和发布：

- A4 页面
- 顶部居中姓名与副标题
- 右上角证件照
- 灰底分节标题
- 科研和项目经历右侧日期列

## 文件结构

- [`cv.tex`](cv.tex)：中文简历主文件
- [`cv_en.tex`](cv_en.tex)：英文简历主文件
- [`resume-format.tex`](resume-format.tex)：中英文共用格式模板
- [`content/cv_zh.tex`](content/cv_zh.tex)：中文内容
- [`content/cv_en.tex`](content/cv_en.tex)：英文内容
- [`assets/headshot.jpg`](assets/headshot.jpg)：头像
- [`.latexmkrc`](.latexmkrc)：默认使用 `xelatex`

## 编译

```bash
./make.sh
```

产物默认输出到 `build/` 目录，其中 `build/cv.pdf` 为中文简历，`build/cv_en.pdf` 为英文简历。也可以传入指定 TeX 文件只编译单个版本，例如 `./make.sh cv_en.tex`。

## 在线版本

每次推送到 `main` 后，GitHub Actions 会编译并部署最新版 PDF：

- 中文版：<https://zhhangbian.github.io/CV/cv.pdf>
- English: <https://zhhangbian.github.io/CV/cv_en.pdf>
- 版本选择页：<https://zhhangbian.github.io/CV/>

## 后续编辑

- 改内容：编辑 [`content/cv_zh.tex`](content/cv_zh.tex) 或 [`content/cv_en.tex`](content/cv_en.tex)
- 改照片：替换 [`assets/headshot.jpg`](assets/headshot.jpg)
- 改版式：优先调整 [`resume-format.tex`](resume-format.tex) 中的 `geometry`、`\SectionBar`、`\EntryTitle`、`\BodyLine`

如果后续内容继续增加，当前模板会自动分页。
