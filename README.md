# Confession wall

## How I got the idea

I looked for a project to create, and then I thought of a place where people could confess anonymously.<br>
And I said to myself that it would be perfect and wouldn't take too much time,
<br>because I wouldn't need to create any accounts for the anonymous.
<br> So I started to think on

## The Plan
I didn't want the hustle to use node.js or anything else than Python I wanted this to be a small project that wouldn't take more than a week to create.
<br>So for that reason and the fact that I didn't suspect more than my family and some friends to use it efficiency isn't been my main priority so I could use things that will make the production much more quickly.
<br>For the same reason I used SQLite yes there could be a race condition problem when too many people post at the same time, but SQLite is easy to use and set up and works great with Python, I will note even though I used SQLite many times it still was a little different from what I usually use(MySQL) when I look back I think it would worth the effort to use MySQL, But I'm too lazy and already thinking on the next project to change it.

***note:*** I tried to cause race conditions with my site and couldn't and some sources on the internet say that can't happen and some the opposite so don't take my word on it do your own research

So I chose Flask over Django as the backend framework, for the same reason that I chose Python and SQLite Flask is very easy to use and deploys quickly, I chose Python so I needed all the speed I could get and a lot of the features that Django offers I didn't want/need to use. personally for bigger and more complex projects, I do use Django over Flask but here I didn't see the reason either.

## the backend

The first thing I did was write the backend, when writing the backend I tried to include some security, I did it just for practice.
<br>I always try to keep my code clean organized and somehow professional, again just for practice, so I tried to keep good functions and variable names and not just x and y.
<br>I always tell myself I should add comments but I almost never do so looking back I should haveץ

## security
As I said I tried to include some security, but I'm sure that I did forget something if I did please tell me I would love to do it better next time.
<br>I used Bcrypt as the hashing algorithm i hashed ofc only the password and I did salt it.
<br>I parameterized every SQL query.
<br>I checked if there could be an XSS attack but Jinja in Flask did all the work and I didn't see a reason to add more.

The next time I work on this site will probably to add brute force and DDoS protection cause right now anyone can use Burp Suite to flood the database with posts and to try to delete other's confessions with brute force.
<br>I will implement this protection by allowing only one post request from each IP every second or something like that.

## The Frontend
I hate writing frontend because I can't design my website like I can write a design in the Frontend but only if I have a picture of it because I can't imagine how it will look, so I just used a minimalist design, not the worst but I wanted to have something unique for this project.
<br>So maybe one day I will come back to change the design(if someone wants to help me with the design I will be more than happy).

## Hosting
Yes, I could choose the easy option and use a hosting service but for learning purposes, I used Ngrok yes it is like a hosting service(a tunnel) and it's easy to set up but I wanted the website to run on my pc:
<br> My static domain I got from Ngrok was:
<br>https://unified-first-rooster.ngrok-free.app/
<br><br>I thought it was cool that the subdomain I got was maybe the first(If someone knows please tell me).
<br>I will host the website on a hosting service maybe with a domain for some time.

## How to install
If you want to run the confession wall on your machine that is very easy:
1. Clone the repo:
   ```sh
   git clone https://github.com/IdanHajbeko/Confession-Wall.git
   ```
2. install the requirements:
   ```sh
      pip install -r requirements.txt
   ```
3. Now just run the Python program
<br>***Note:*** You might want to reset/delete the database.db because it will have all of the data from when I used it
## What I would add
When I continue working on this project I will add:
1. Way to search confessions
2. Way to filter confessions posts that aren't confessions because right now one can write anything.
3. Brute force protection 
4. DDoS protection
5. Confessions categories
6. Changing the style
## How to contribute to this project
If you want to contribute to this project by helping:
1. designing
2. writing and bettering the frontend
3. writing and bettering the back end
4. or anything
Contact me through:
1. email: idancode.hajbeko@gmail.com
2. discord: 1idan1
3. or just create a pull request here
<br>I will be happy for any help
