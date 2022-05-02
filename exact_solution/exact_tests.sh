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

echo TEST C APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_c.txt)
echo TEST C APPROX - expected: 3

echo ----------------------------

# complete graph with 8 nodes, takes around 30 seconds
echo TEST D EXACT - output: $(time python3 cs412_np_exact.py < test_cases/test_d.txt)
echo TEST D EXACT - expected: 8

echo TEST D APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_d.txt)
echo TEST D APPROX - expected: 8

echo ----------------------------

echo TEST E EXACT - output: $(time python3 cs412_np_exact.py < test_cases/test_e.txt)
echo TEST E EXACT - expected: 3

echo TEST E APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_e.txt)
echo TEST E APPROX - expected: 3

echo ----------------------------

# one node
echo TEST F EXACT - output: $(time python3 cs412_np_exact.py < test_cases/test_f.txt)
echo TEST F EXACT - expected: 1

echo TEST F APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_f.txt)
echo TEST F APPROX - expected: 1

echo ----------------------------

# five nodes with zero edges
echo TEST G EXACT - output: $(time python3 cs412_np_exact.py < test_cases/test_g.txt)
echo TEST G EXACT - expected: 1

echo TEST G APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_g.txt)
echo TEST G APPROX - expected: 1

echo ----------------------------

# three sets of two nodes connected by one edge
echo TEST H EXACT - output: $(time python3 cs412_np_exact.py < test_cases/test_h.txt)
echo TEST H EXACT - expected: 2

echo TEST H APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_h.txt)
echo TEST H APPROX - expected: 2

# echo ----------------------------

# complete graph with 9 nodes, takes around 15 minutes
# echo TEST I EXACT - output: $(time python3 cs412_np_exact.py < test_i.txt)
# echo TEST I EXACT - expected: 3

# echo TEST I APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_i.txt)
# echo TEST I APPROX - expected: 3

# echo ----------------------------

# this test will take around 40 minutes
# echo TEST J EXACT - output: $(time python3 cs412_np_exact.py < test_cases/test_j.txt)
# echo TEST J EXACT - expected: 9

# echo TEST J APPROX - output: $(time python3 ../approximation_solution/cs412_mingraph_approximation_a.py < test_cases/test_j.txt)
# echo TEST J APPROX - expected: 9
