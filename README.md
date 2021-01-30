# Thinkcode
Thinkcode is a platform centered towards assisting programmers, more specifically,
computer science students. It provides tools that will not only increase their
productivity, such as quickly open a webpage directly on our software and a quick 
Wi-Fi speed test, but also to improve their learning experience with our quizzing feature.
Using Natural Language Processing, our AI creates relevant questions based on a topic provided
by the user. Thinkcode is the solution for innovative students and programmers.

## How to run
Download the contents of this repository and first run `pip install requirements.txt`.
Then, if not already installed, run `pip install pyaudio` and also `python3 -m spacy download en_core_web_sm`.

After downloading all the necessary packages, run `python app.py`. 

## Important notes:
- If you get the following error (or similar) when asking for internet speed: `ERROR: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)>
`, if you're using macOS go to Macintosh HD > Applications > Python3.8 (or whichever Python version you're using) and click on the file "Install Certificates.command"

## Tasks that the AI can perform:

#### General Functionalities
1. Date and time
    - `Human: What time is it?`
    - `Human: What day is it?`
2. Joke
    - `Human: Tell me a joke`
3. Internet Connection Speed
    - `Human: What is my Wi-Fi speed?`
    - `Human: How does my internet speed look like?`
4. Documentation for any technology or programming language
    - `Human: Documentation for Python`
    - `Human: Documentation for Angular`
    - `Human: Documentation for Flask`
5. Git Cheat-Sheet
    - `Human: Open git cheat-sheet`
6. StackOverflow search
    - `Human: Search Stack Overflow for Value Type Error in Python`
7. YouTube search
    - `Human: Search youtube for Tech With Tim`
8. Google search
    - `Human: Search for Tech With Tim Tutorials`
9. Open page
    - `Human: Open GitHub`
    - This functionality works for the following web pages:
        1. W3schools
        2. YouTube
        3. GitHub
        4. Stack Overflow
        5. Google
        6. Git
        7. GitLab
        8. Algo Expert
        9. LeetCode
        10. Codewars
        11. Linux's webpage
10. Wikipedia Lookups
    - `Human: Who is Bill Gates?`
    - `Human: What is Object Oriented Programming?`

### Quizing
This AI also has a quizzing functionality, and given a topic it will create a
quiz based on the keysentences and keywords of an article. They are determined
using NLP (Natural Language Processing), with the modules `pytextrank` and `rake_nltk`.

To be quized: `Human: Quiz me on <QUIZ TOPIC>`

Then the AI will tell you sentences, and you will be needed to fill in the blank. After
answering all questions, you'll receive a grade based on your performance.

### Note-taking
Make notes
    - `Human: new note study plan`
    - To look at the note, just go to the directory and open the markdown file

#### Mathematical Functionalities
This virtual assistant can also perform mathematical operations
ranging from checking if a number is prime, to trigonometry calculations,
to basic algebra and more.

Important note: If the desired operation is long and uses a more complex function,
such as a square root and trigonometry, what is 'inside' the brackets will
range from right after the human asks for it until the end of the sentence.

For instance:
`Human: What is the square root of 9 multiplied by 3`

The AI will understand this as: `square root of (9 * 3)`

#### Mathematical Operations
1. Basic Arithmetic
    1. Addition: `Human: What is 5 plus 3`
    2. Subtraction: `Human: What is 4 minus 2`
    3. Multiplication: `Human: What is 12 multiplied by 2`
    4. Division: `Human: What is 9 divided by 3`
2. Powers and Roots
    1. Exponents: `Human: What is 4 to the power of 2`
    2. Square Roots: `Human: What is the square root of 9`
3. Multiple Arithmetic Operations
    1. Combining addition and subtraction: `Human: What is 5 plus 2 minus 1`
    2. Combining multiplication and division: `Human: What is 5 multiplied by 2 divided by 3`
    3. Several Arithmetic Operations: `Human: What is 5 multiplied by 2 plus the square root of 9`
4. Prime Numbers:
    1. Prime number checker: `Human: Is 41 a prime number?`
    2. Generate list of prime numbers: `Human: Generate list of prime numbers between 1 and 10`
5. Trigonometry:
    1. Cosine: `Human: What is the cosine of 3`
    2. Sine: `Human: What is the sine of 2`
    3. Tangent: `Human: What is the tangent of 4`
    

## Libraries that are required to be installed:
- Pyttsx3
- SpeechRecognition
- Pyaudio
- speedtest-cli
- wikipedia
- webbrowser
- spacy
- pytextrank
- rake_nltk

To download all using Pip, `cd` into the directory where `requirements.txt`
is located, run:
`pip install -r requirements.txt`
(requirements file coming soon)

## In-Build libraries that need to be imported
- datetime
- re
- random
- math
- json