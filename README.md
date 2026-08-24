# LaTeX CV

这个仓库把 [`ref/cv.pptx`](/Users/bian/Desktop/project/cv/ref/cv.pptx) 转成了可维护的 XeLaTeX 简历项目，保留了原稿的核心排版特征，同时允许内容自然分页，方便后续继续扩展：

- A4 页面
- 顶部居中姓名与副标题
- 右上角证件照
- 灰底分节标题
- 科研和项目经历右侧日期列

## 文件结构

- [`cv.tex`](/Users/bian/Desktop/project/cv/cv.tex)：中文简历主文件
- [`cv_en.tex`](/Users/bian/Desktop/project/cv/cv_en.tex)：英文简历主文件
- [`resume-format.tex`](/Users/bian/Desktop/project/cv/resume-format.tex)：中英文共用格式模板
- [`content/cv_zh.tex`](/Users/bian/Desktop/project/cv/content/cv_zh.tex)：中文内容
- [`content/cv_en.tex`](/Users/bian/Desktop/project/cv/content/cv_en.tex)：英文内容
- [`assets/headshot.jpg`](/Users/bian/Desktop/project/cv/assets/headshot.jpg)：从 PPTX 提取的照片
- [`.latexmkrc`](/Users/bian/Desktop/project/cv/.latexmkrc)：默认使用 `xelatex`

## 编译

```bash
./make.sh
```

产物默认输出到 `build/` 目录，其中 `build/cv.pdf` 为中文简历，`build/cv_en.pdf` 为英文简历。也可以传入指定 TeX 文件只编译单个版本，例如 `./make.sh cv_en.tex`。

## 后续编辑

- 改内容：编辑 [`content/cv_zh.tex`](/Users/bian/Desktop/project/cv/content/cv_zh.tex) 或 [`content/cv_en.tex`](/Users/bian/Desktop/project/cv/content/cv_en.tex)
- 改照片：替换 [`assets/headshot.jpg`](/Users/bian/Desktop/project/cv/assets/headshot.jpg)
- 改版式：优先调整 [`resume-format.tex`](/Users/bian/Desktop/project/cv/resume-format.tex) 中的 `geometry`、`\SectionBar`、`\EntryTitle`、`\BodyLine`

如果要继续逼近原始 PPT 的视觉效果，最值得继续收的是字号、段间距和顶部照片块比例。
如果后续内容继续增加，当前模板会自动分页，不需要再回到 PPT 里手动挪版。
