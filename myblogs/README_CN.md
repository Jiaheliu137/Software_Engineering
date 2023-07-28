

[English](.././README.md)|简体中文

**这个项目用django建立了一个博客网站**

# MyBlogs Tech Spec Document

## 0.Use

打开终端，依次执行下面的命令

```bash
git clone https://github.com/Jiaheliu137/Software_Engineering
cd Software_Engineering/myblogs
pip install poetry
poetry install
```

```python
poetry shell
python manage.py runserver
```

**管理员账户：**

**用户名: admin**

**密码: admin123456**

下次继续运行该项目的时候要首先进入项目文件夹，再运行`poetry shell`

## 1. Introduction

"MyBlogs" 是一个基于 Python Django 框架构建的简单博客应用。它允许用户注册、登录、查看作者的博客文章、搜索文章、根据日期筛选文章，以及发布、编辑和删除自己的博客文章。

## 2. Models

该项目定义了以下两个模型：

- `Author`：代表博客作者。每个作者关联一个 Django 用户对象，每个用户可以写多篇博客文章。
- `Post`：代表博客文章。每篇文章有一个标题，内容，创建日期，以及关联的作者。

## 3. Views

项目包含以下视图：

- `login`：处理用户登录。
- `logout`：处理用户登出。
- `register`：处理用户注册。
- `author_list`：显示所有作者的列表。
- `author_posts`：显示一个特定作者的所有文章。
- `post_list`：显示所有文章的列表。
- `post_detail`：显示一篇特定文章的详细信息。
- `new_post`：允许用户创建新的文章。
- `post_delete`：允许用户删除他们自己的文章。
- `search`：搜索文章
- `user_center`：显示用户中心，包括用户的信息和他们发布的文章。

## 4. Templates

项目使用了以下模板：

- `base.html`：所有其他模板的基础模板
- `author_list.html`：用于显示所有作者的列表。
- `author_posts.html`：用于显示一个特定作者的所有文章。
- `post_list.html`：用于显示所有文章的列表。
- `post_detail.html`：用于显示一篇特定文章的详细信息。
- `new_post.html`：用于创建新的文章。
- `post_delete.html`：用于删除文章。
- `search_results.html`：用于显示文章搜索结果。
- `date_posts.html`：用于显示在特定日期范围内发布的文章。
- `login.html`：用于处理用户登录。
- `register.html`：用于处理用户注册。
- `user_center.html`：用于显示用户中心，包括用户的信息和他们发布的文章。

## 5. Functionality

- **浏览网站**：即使没有账户也可以浏览网站

- **选择页码**：用户可以直接previous和next翻页，也可以直接点击页码或者输入页码进行跳转

  - 页码会显示当前页面的前后三页

- **注册和登录**：用户可以注册新账号并登录。

- **用户列表**：显示所有注册过的用户

- **修改个人信息**：在用户界中心可以更改个人信息

- **浏览文章**：可以在网站主页点击文章标题浏览文章，也可以

- **发布、编辑和删除文章**：已登录的用户可以发布新文章，以及删除他们自己的文章。

  - 普通用户只能删除自己的文章
    - 提示是否删除，是的话则删除后直接回到网站主页；否的话则返回当前文章
    
  - 管理员可以直接删除所有文章

  - 使用bleach库来过滤敏感html标签，保留了一些安全的标签和属性供用户使用以提升编辑自由度
    可以使用的标签和属性有：

    ```python
    >>> ALLOWED_TAGS
    frozenset({'acronym', 'pre', 'em', 'span', 'i', 'abbr', 'table', 'li', 'blockquote', 'h4', 'h2', 'div', 'th', 'img', 'thead', 'br', 'ol', 'tbody', 'strong', 'td', 'b', 'h3', 'h1', 'code', 'tr', 'a', 'h5', 'p', 'ul', 'h6'})
    >>> ALLOWED_ATTRIBUTES
    {'a': ['href', 'rel', 'target'], 'abbr': ['title'], 'acronym': ['title'], 'img': ['src', 'alt']}
    >>> 
    ```

    其他标签不会被渲染只会显示字符串形式

- **查看作者文章**：用户可以查看特定作者的所有文章。

- **搜索文章**：用户可以通过关键词搜索文章标题和作者。

  - 直接搜索：会搜索网站的所有文章
  - 在搜索结果中按时间过滤：只会在搜索结果中过滤文章

- **过滤文章**：用户可以按时间过滤文章

  - 直接过滤：过滤网站所有文章
  - 在过滤结果中搜索：可以在过滤结果中搜索


## 未来可能对项目的优化：

- 完善UI界面 
- 增加评论功能 
- 增加文章修改功能 
- 增加文章中插入图片的功能 
- 增加标签功能，用户可以给文章打标签从而分类



