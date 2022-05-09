(define 
(problem m2wr_cluedo)
(:domain m2wr_cluedo)
(:objects
    marker1 marker2 oracle - location
    nav - navigation_token
    hnt - hint
    hyp - hypothesis
    gm - game
)
(:init
    (at marker1) 
    (not_at marker2)
    (not_at oracle)
    (proceed_investigate nav)
    (no_same_location marker1 marker2)
    (no_same_location marker1 oracle)
)
(:goal(
    and
    (not_at marker1)
    (game_finished gm )
)
    ;(consistent_hypothesis hyp)
    
)
)