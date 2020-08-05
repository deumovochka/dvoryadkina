# EDA students academic performance in math

## Goal: to make EDA of data with different parameters that can affect on student's score in math
Data contains 3 quantitative variables - age, absences, score, and all other nominative variables.

## Conclusions:
- All empty values were filled in, the data became complete.
- Outliers were only found in the column "age" and "absences", but all values are left out of common sense.
- A negative correlation between score and age tells us that the score worsens with age, and a negative correlation between score and absences tells us that the more gaps, the lower the score. Both conclusions are quite logical.
- The most important parameters that we will leave for building a further model are age, absences, address, Medu, Fedu, Mjob, Fjob, failures, paid, higher, romantic, studytime, schoolsup, goout.
