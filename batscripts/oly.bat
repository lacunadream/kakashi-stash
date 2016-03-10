@echo off
SET x=%CD%
C:
cd C:\Users\David\AppData\Custom
IF "%1"=="-list" (
 @echo on
 dir *.bat
 @echo off
 cd/D %x%
)
