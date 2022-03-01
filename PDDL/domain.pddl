(define (domain m2wr_cluedo)
    (:requirements :strips ::durative-actions)
    (:types
        location
        hint
        hypothesis
        response
        navigation_token
        game
    )
    (:predicates
        (at ?loc - location)
        (hint_found ?hnt - hint)
        (consistent_hypothesis ?hyp - hypothesis)
        (oracle_res ?res - response)
        (is_oracle ?loc - location)
        (proceed_investigate ?nav - navigation_token)
        (no_same_location ?from ?to - location)
        (game_finished ?gm - game)

    )

    (:durative-action navigation
        :parameters (?nav - navigation ?from ?to- location)
        :duration (= ?duration 1)
        :condition (and 
            (at start (and
                    (proceed_investigate ?nav - navigation_token)
                    (no_same_location ?from ?to - location)
                    (at ?from - location)
            ))
        )
        :effect (and
            (at end (and
                    (not (proceed_investigate ?nav - navigation_token))
                    (hint_found ?hnt - hint)
                    (at ?to - location)
                    (not (at ?from - location))
            ))
        )
    )
    

    (:durative-action reason
    :duration (= ?duration 1)
    :parameters (?hnt - hint)
    :precondition (and 
        (at start
            (hint_found ?hnt - hint)
        )
        
        )
    :effect (and
        (at end and(
                (not (hint_found ?hnt - hint))
                (consistent_hypothesis ?hyp)
                )
            )
        )
    )


    (:durative-action oracle
    :duration (= ?duration 1)
    :parameters (?from ?to - location ?hyp - hypothesis ?gm - game)
    :precondition (and
        (at start
            and(
                (no_same_location ?from ?to - location)
                (at ?from - location)
                (is_oracle ?loc - location)
                (consistent_hypothesis ?hyp- hypothesis)
            ))
        )
    :effect (and
        (at end 
            and(
                (at ?to - location)
                (not (at ?from - location))
                (game_finished ?gm - game)
            )
        ))
    )

    
)