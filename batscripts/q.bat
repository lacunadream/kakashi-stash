@echo off
D:
cd D:/Coding/Github/qriousity/mvp
IF "%1"=="-up" (
 nodemon app.js
)	
