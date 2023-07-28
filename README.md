English|**[简体中文](./myblogs/README_CN.md)**

This repo is used to record Sourse:Software Engineering for Internet Applications

**The project builds a blog website using Django.**

# Tech Spec Document

## 0. Use

Open the terminal and execute the following commands one by one.

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

**The administrator's**

**accoount name: admin**

**passward: admin123456**

When continuing to run this project in the future, you need to first enter the project directory and then use the command `poetry shell`

## 1. Introduction

"MyBlogs" is a simple blog application built with the Python Django framework. It allows users to register, log in, view blog posts by authors, search for posts, filter posts by date, as well as post, edit, and delete their own blog posts.

## 2. Models

The project defines the following two models:

- `Author`: Represents the blog author. Each author is associated with a Django user object, and each user can write multiple blog posts.
- `Post`: Represents the blog post. Each post has a title, content, creation date, and associated author.

## 3. Views

The project includes the following views:

- `login`: Handles user login.
- `logout`: Handles user logout.
- `register`: Handles user registration.
- `author_list`: Displays a list of all authors.
- `author_posts`: Displays all posts by a specific author.
- `post_list`: Displays a list of all posts.
- `post_detail`: Displays detailed information about a specific post.
- `new_post`: Allows users to create new posts.
- `post_delete`: Allows users to delete their own posts.
- `search`: Searches for posts.
- `user_center`: Displays the user center, including user information and their posts.

## 4. Templates

The project uses the following templates:

- `base.html`: The base template for all other templates.
- `author_list.html`: Used to display a list of all authors.
- `author_posts.html`: Used to display all posts by a specific author.
- `post_list.html`: Used to display a list of all posts.
- `post_detail.html`: Used to display detailed information about a specific post.
- `new_post.html`: Used to create new posts.
- `post_delete.html`: Used to delete posts.
- `search_results.html`: Used to display post search results.
- `date_posts.html`: Used to display posts published within a specific date range.
- `login.html`: Used to handle user login.
- `register.html`: Used to handle user registration.
- `user_center.html`: Used to display the user center, including user information and their posts.

## 5. Functionality

- **Website Browsing**: The site can be browsed even without an account.

- **Page Selection**: Users can navigate through pages using the previous and next buttons, or directly click on or input page numbers to jump to a particular page.

  - The page number will display three pages before and after the current page.

- **Registration and Login**: Users can register for a new account and log in.

- **User List**: Displays all registered users.

- **Modify Personal Information**: Personal information can be changed in the user center.

- **Browsing Articles**: Articles can be viewed by clicking on the article title on the homepage.

- **Posting, Editing, and Deleting Articles**: Logged-in users can publish new articles and delete their own articles.

  - Regular users can only delete their own articles.
    - A prompt will ask if they want to delete, and if confirmed, the article will be deleted, and the user will be redirected to the main website homepage. If canceled, the user will stay on the current article page.
    
  - Administrators have the privilege to directly delete all articles.

  - The "bleach" library is used to filter sensitive HTML tags, allowing users to utilize certain safe tags and attributes to enhance editing flexibility.
    The allowed tags and attributes are: [list the allowed tags and attributes here]
    
    ```python
    ALLOWED_TAGS
    frozenset({'acronym', 'pre', 'em', 'span', 'i', 'abbr', 'table', 'li', 'blockquote', 'h4', 'h2', 'div', 'th', 'img', 'thead', 'br', 'ol', 'tbody', 'strong', 'td', 'b', 'h3', 'h1', 'code', 'tr', 'a', 'h5', 'p', 'ul', 'h6'})
     ALLOWED_ATTRIBUTES
    {'a': ['href', 'rel', 'target'], 'abbr': ['title'], 'acronym': ['title'], 'img': ['src', 'alt']}
    ```
    
    Other tags will not be rendered, they will only display as string forms.
    
    

- **Viewing Author's Articles**: Users can view all articles by a specific author.

- **Searching for Articles**: Users can search for articles by keywords in the title and author.

  - Direct Search: This will search all articles on the site.
  - Filtering by time within search results: This will only filter articles within the search results.

- **Filtering Articles**: Users can filter articles by date.

  - Direct Filtering: This will filter all articles on the site.

## 6.Possible future optimizations for the project:
- Enhance the UI interface.
- Add a commenting feature.
- Implement article editing functionality.
- Enable the ability to insert images into articles.
- Introduce tagging functionality, allowing users to categorize articles by assigning tags.

