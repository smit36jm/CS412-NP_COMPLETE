#!/bin/sh
echo TEST A EXACT - output: $(time python3 cs412_np_exact.py < test_cases/test_a.txt)
echo TEST A EXACT - expected: 3

echo TEST A APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_a.txt)
echo TEST A APPROX - expected: 3

echo ----------------------------

echo TEST B EXACT - output: $(time python3 cs412_np_exact.py < test_cases/test_b.txt)
echo TEST B EXACT - expected: 3

echo TEST B APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_b.txt)
echo TEST B APPROX - expected: 3

echo ----------------------------

echo TEST C EXACT - output: $(time python3 cs412_np_exact.py < test_cases/test_c.txt)
echo TEST C EXACT - expected: 3

#takes around 30 seconds
echo TEST C APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_c.txt)
echo TEST C APPROX - expected: 3

# 15 minutes??
# echo TEST 9 - output: $(time python3 cs412_np_exact.py < test_9.txt)
# echo TEST 9 - expected: 3
