(define (problem m2wr_cluedo_problem)
    (:domain m2wr_cluedo)
    (:objects
        marker1 - location
        marker2 - location
        marker3 - location
        marker4 - location
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
        
    )
    (:goal

        (game_finished gm )
    )
)