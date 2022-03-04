(define (problem task)
(:domain m2wr_cluedo)
(:objects
    marker1 marker2 marker3 marker4 oracle - location
    hnt - hint
    hyp - hypothesis
    nav - navigation_token
    gm - game
)
(:init
    (at marker1)



    (is_oracle oracle)

    (proceed_investigate nav)

    (no_same_location marker1 marker2)
    (no_same_location marker2 marker3)
    (no_same_location marker3 marker4)
    (no_same_location marker1 oracle)
    (no_same_location marker2 oracle)
    (no_same_location marker3 oracle)
    (no_same_location marker4 oracle)


)
(:goal (and
    (hint_found hnt)
))
)
