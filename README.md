##Pattern-Matching Paths 


###Problem Statement 

You've been given two lists: the first is a list of patterns, the second 
is a list of slash-separated paths. Your job is to print, for each path, 
the pattern which best matches that path. ("Best" is defined more 
rigorously below, under "Output Format".) 

A pattern is a comma-separated sequence of non-empty fields. For a 
pattern to match a path, every field in the pattern must exactly match 
the corresponding field in the path. (Corollary: to match, a pattern and 
a path must contain the same number of fields.) 

For example: the pattern x,y can only match the path x/y. Note, however, that leading and trailing slashes in paths should be ignored, thus x/y and /x/y/ are equivalent. 

Patterns can also contain a special field consisting of a single 
asterisk, which is a wildcard and can match any string in the path. 
For example, the pattern `A,*,B,*,C` consists of five fields: three 
strings and two wildcards. It will successfully match the paths 
`A/foo/B/bar/C` and `A/123/B/456/C`, but not `A/B/C`, 
`A/foo/bar/B/baz/C`, or `foo/B/bar/C`. 

#####Input Format 

The first line contains an integer, N, specifying the number of 
patterns. The following N lines contain one pattern per line. You may 
assume every pattern is unique. The next line contains a second integer, 
M, specifying the number of paths. The following M lines contain one 
path per line. Only ASCII characters will appear in the input. 

#####Output Format 

For each path encountered in the input, print the best-matching 
pattern. The best-matching pattern is the one which matches the path 
using the fewest wildcards. 

If there is a tie (that is, if two or more patterns with the same number 
of wildcards match a path), prefer the pattern whose leftmost wildcard 
appears in a field further to the right. If multiple patterns' leftmost 
wildcards appear in the same field position, apply this rule recursively 
to the remainder of the pattern. 

For example: given the patterns `*,*,c` and `*,b,*`, and the path 
`/a/b/c/`, the best-matching pattern would be `*,b,*`. 

If no pattern matches the path, print NO MATCH. 

#####Submission Requirements 

You should submit a working program, runnable from a command line, that 
reads from standard input and prints to standard output. In Unix 
parlance, for example, it should be runnable like this: 

cat input_file | python your_program.py > output_file 

Of course, the actual command line may vary depending on the language 
you choose; your program file need not be executable on its own. 
However, it must read input directly from stdin and print to stdout. 

You may write your program in any of the following languages:  
JavaScript (Node.js)  
Python (2.7 or 3.x)  
Java

#####Extra Credit 
What's the algorithmic complexity of your program? In other words, how 
does its running time change as the number of patterns or number of 
paths increases? 

Would your program complete quickly even when given hundreds of 
thousands of patterns and paths? Is there a faster solution? 

Hint: although a correct program is sufficient, there is extra credit 
for an algorithm that's better than quadratic. Some of our test cases 
are very large. To pass them all, your program will need to be pretty 
fast! 

#####Example Input 

```
6  
*,b,*   
a,*,*  
*,*,c  
foo,bar,baz   
w,x,*,*  
*,x,y,z  
5  
/w/x/y/z/   
a/b/c  
foo/  
foo/bar/   
foo/bar/baz/   
```
#####Example Output 
```
*,x,y,z   
a,*,*  
NO MATCH   
NO MATCH  
foo,bar,baz 
```

#####Tips 

- Code correctness and quality matter more to us than algorithmic wizardry. Is your program easy to understand? Is it clearly organized and documented? Does it correctly handle all the edges cases? Imagine you are writing a library for other developers to use. How would that affect your design? 

- Your program's output must precisely match the expected output. Don't print extraneous or superfluous stuff to stdout. 

- The example input and output provided above fail to cover a large number of edge cases. To be sure your program is correct, you may want to supplement it with your own test cases. 

- Every line in the input ends with a Unix-style newline ("\n"). DOS-style CRLFs ("\r\n") are not used. 

- Each line in the output should end with a newline character (that includes the final one). As with the input, use Unix-style newlines.


---
####Solution
The code to execute the pattern matching algorithm for sample input and a custom set of input has already been placed 
inside `run.sh`. In order to execute the same, just launch terminal and `cd` into the current directory.
From the terminal run
```bash
source run.sh
```
This would perform the pattern matching on basis of input files `test_input/sample_input` and `test_input/custom_input` 
and place the corresponding output in `sample_output` and `custom_output` respectively.
Do note that the bash script removes any existing output files in the directory.

In order to run a custom file against the codebase, run the following from terminal:
```bash
cd /path/to/current/dir/
cat /path/to/input/file/ | python3 src/run.py > /path/to/output/file/
```

---

####Code Complexity
The input patterns are grouped into patterns of same length. Therefore, while performing a search
for the closest matching pattern, the validation is done only against the patterns that match the length of the source
path. In this manner the actual complexity `m*n` is reduced by a factor of the number of patterns lengths.
So, effectively, if the `m` patterns are spread across `l` number of lengths, the complexity would be more like `m*n/l`.

In order to further reduce the complexity, the patterns groups can be sub-grouped into patterns with similar wildcard
 counts. In this manner, the search would then be performed upon the patterns with no wildcards (wildcard_count=0)
 first, then on patterns with wildcard count of 1, then 2 and so on. The first matching pattern in this order would be 
 the closest match. The overhead in this approach would be while adding the patterns to the pattern groups but the 
 resulting time optimization would far outweigh the time taken for extremely large data-sets.

Note: The optimization mentioned above has not been implemented in the code due to shortage of time.
Just to show a representation, current PatternMap dictionary of structure:
```python
{
    3: ['a,*,*'],
    4: ['a,b,c,d', 'a,b,*,d', 'a,b,*,*', 'a,*,*,d', '*,*,*,*']
}
```
would change to:
```python
{
    3: {
        2: ['a,*,*']
    },
    4: {
        0: ['a,b,c,d'],
        1: ['a,b,*,d'],
        2: ['a,b,*,*', 'a,*,*,d'],
        4: ['*,*,*,*']
    }
}
```
and search for paths of length 4 would be performed on patterns in order `pattern_group[4][0]` 
then `pattern_group[4][1]`
then `pattern_group[4][2]`
then `pattern_group[4][4]`, thereby reducing the number of searches significantly.


