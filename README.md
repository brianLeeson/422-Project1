# 422-Project1
This is the first group project for CIS 422 Software Methodologies course.
The project authors are:
1. Brian Leeson
2. Jamie Zimmerman
3. Amie Corso

### Description:
This project attempts to solve the problem of sorting student into groups for the 422 course.
Students are asked to fill out a short survey about themselves and are sorted into groups
based on survey data. We use python3 to sort students into teams and a GUI made with the tk library
to interface with the user.

### Dependencies:
This project has been set up to run in a virtual environment in order to support installations on 
platforms where the user may not have root permissions and to better insulate this project from the
host machine. If the project we to be extended, instructions have been left in the Makefile on how
to add dependencies in the virtual environment.
git  
python 3.*  
bash shell  

### Instructions:  
Setup:
 * make sure all dependencies are installed.
 * "git clone https://github.com/brianLeeson/422-Project1"
 * survey available at: https://tinyurl.com/422formsurvey. modifications are not supported.
 * remove previous survey results before sending out new surveys.
 * send the survey to students by clicking the "Send" button at the top.
 * after all responses are gathered, export the google form to csv  
 
To run the application:
 * run the application with "make run".
 * import the survey results csv
 * sort students into teams
 * optionally export sorted teams to csv for review.
 
 
