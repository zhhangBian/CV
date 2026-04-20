# LaTeX CV

这个仓库把 [`ref/cv.pptx`](/Users/bian/Desktop/project/cv/ref/cv.pptx) 转成了可维护的 XeLaTeX 简历项目，保留了原稿的核心排版特征，同时允许内容自然分页，方便后续继续扩展：

- A4 页面
- 顶部居中姓名与副标题
- 右上角证件照
- 灰底分节标题
- 科研和项目经历右侧日期列

## 文件结构

- [`cv.tex`](/Users/bian/Desktop/project/cv/cv.tex)：主文件
- [`assets/headshot.jpg`](/Users/bian/Desktop/project/cv/assets/headshot.jpg)：从 PPTX 提取的照片
- [`.latexmkrc`](/Users/bian/Desktop/project/cv/.latexmkrc)：默认使用 `xelatex`

## 编译

```bash
latexmk -xelatex cv.tex
```

产物默认输出到 `build/` 目录。

## 后续编辑

- 改内容：直接编辑 [`cv.tex`](/Users/bian/Desktop/project/cv/cv.tex) 中各 section 文本
- 改照片：替换 [`assets/headshot.jpg`](/Users/bian/Desktop/project/cv/assets/headshot.jpg)
- 改版式：优先调整 `geometry`、`\SectionBar`、`\DateLine`、`\BodyLine`

如果要继续逼近原始 PPT 的视觉效果，最值得继续收的是字号、段间距和顶部照片块比例。
如果后续内容继续增加，当前模板会自动分页，不需要再回到 PPT 里手动挪版。
