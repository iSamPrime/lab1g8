# lab1g8
DAT395 / DIT014 Fundamentals of program development - Lab 1: Word Counting - Group 8 


## Git Commands
### …or create a new repository 
```
git init
git add README.md
git commit -m "first commit"
git branch -M main # replace "main" with the new branch name 
git remote add origin https://github.com/iSamPrime/lab1g8.git
git push -u origin main
```



### …or pull an existing repository 
```
git remote add origin https://github.com/iSamPrime/lab1g8.git
git branch -M main
git pull origin main 
```
### …or commit to an existing repository/branch
```
git add filename.txt   # Stage a specific file
git add .              # Stage all changes in the current directory
git commit -m "message" # change the message of what you have done
git status 
git push origin main # pushes to the branch "main"
```

### …how to log in git in the terminal 
```
git config user.name my-name
git config user.email my-email@gmail.com
```

Skapa en Token på GitHub
1. Logga in på GitHub.com.
2. Klicka på din profilbild uppe till höger och välj Settings.
3. Scrolla ner i vänstermenyn och klicka på Developer settings.
4. Klicka på Personal access tokens och välj Tokens (classic).
5. Klicka på Generate new token → Generate new token (classic).
6. Ge token ett namn (t.ex. "Skoldator") och välj utgångsdatum.
7. Markera kryssrutan repo (detta ger tillgång till dina kodarkiv).
8. Klicka på Generate token längst ner.
9. Kopiera koden direkt! Du kommer inte kunna se den igen.

```
git push -u origin main
```

Password: Klistra in din Token (inte ditt vanliga lösenord). Obs: Det syns inga tecken eller stjärnor när du klistrar in i terminalen, det är helt normalt. Tryck bara på Enter.