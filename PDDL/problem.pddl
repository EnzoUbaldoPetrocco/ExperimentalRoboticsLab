(define (problem m2wr_cluedo_problem)
    (:domain m2wr_cluedo)
    (:objects
        marker1 marker2 marker3 marker4 oracle - location
        nav - navigation_token
        hnt - hint
        hyp - hypothesis
        gm - game
    )
    (:init
        (at marker1) 
        (proceed_investigate nav)
        (no_same_location marker1 marker2)
        (no_same_location marker2 marker3)
        (no_same_location marker3 marker4)
        (no_same_location marker1 oracle)
        (no_same_location marker2 oracle)
        (no_same_location marker3 oracle)
        (no_same_location marker4 oracle)
        (is_oracle oracle)
    )
    (:goal(
        and
            (hint_found hnt)
    )
        ;(at marker1)
        ;(hint_found hnt)
        ;(consistent_hypothesis hyp)
        ;(game_finished gm )
    )
)