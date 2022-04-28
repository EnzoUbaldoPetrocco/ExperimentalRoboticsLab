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

    (not_at marker2)
    (not_at marker3)
    (not_at marker4)
    (not_at oracle)



    (is_oracle oracle)

    (proceed_investigate nav)

    (no_same_location marker1 marker2)
    (no_same_location marker1 marker3)
    (no_same_location marker1 marker4)
    (no_same_location marker1 oracle)



)
(:goal (and
    (game_finished gm)
    (not_at marker1)
))
)
