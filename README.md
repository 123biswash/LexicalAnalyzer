# The python pr01 example

One time setup

    $ cd python-example
    $ virtualenv --no-site-packages env

Beginning your work session (you only need to do this once per terminal session)

    $ source activate.sh

your next prompt should be prefixed by (env)

    (env) $

(One time) Install the third party requirements for testing

    (env) $ pip install -r requirements.txt

Running the tests

    (env) $ pytest -v

Running the program

    (env) $ echo "asdfasd asdf a" | pr01 ../examples/0-ex-program.ns
    Config(nfa_program='0 SPLIT 1 4\n1 CHAR 97 97\n2 CHAR 97 97\n3 MATCH\n4 SPLIT 5 10\n5 CHAR 97 97\n6 SPLIT 7 9\n7 CHAR 97 97\n8 JMP 6\n9 MATCH\n10 SPLIT 11 13\n11 CHAR 32 32\n12 JMP 17\n13 SPLIT 14 16\n14 CHAR 9 9\n15 JMP 17\n16 CHAR 10 10\n17 SPLIT 18 26\n18 SPLIT 19 21\n19 CHAR 32 32\n20 JMP 25\n21 SPLIT 22 24\n22 CHAR 9 9\n23 JMP 25\n24 CHAR 10 10\n25 JMP 17\n26 MATCH\n', input='asdfasd asdf a\n')

Adding new third party packages:

    (env) $ echo "package-name" >> requirements.txt
    (env) $ pip install -r requirements.txt

Running the student-grader script:

    $ ../bin/student-grader ./bin/pr01

Initially your score will be 0%:

    ------------------------------------------------------------------------------
                                               score: 0.00%, passed: 0, failed: 19
