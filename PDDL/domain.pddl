(define (domain m2wr_cluedo)
    (:requirements :strips :typing :durative-actions)
    (:types
        location
        hint
        hypothesis
        navigation_token
        game
    )
    (:predicates
        (at ?loc - location)
        (hint_found ?hnt - hint)
        (consistent_hypothesis ?hyp - hypothesis)
        (is_oracle ?loc - location)
        (proceed_investigate ?nav - navigation_token)
        (no_same_location ?from ?to - location)
        (game_finished ?gm - game)

    )

    (:durative-action navigation
        :parameters (?nav - navigation ?from ?to - location ?hnt - hint)
        :duration (= ?duration 1)
        :condition 
            (at start (and
                    (proceed_investigate ?nav)
                    (no_same_location ?from ?to)
                    (at ?from)
            )
        )
        :effect (and
            (at end (and
                    (not (proceed_investigate ?nav))
                    (at ?to)
                    (not (at ?from))
            ))
        )
    )


    (:durative-action find_hint
        :parameters (?nav - navigation ?loc - location ?hnt - hint)
        :duration (= ?duration 1)
        :condition 
            (at start (and
                    (at ?loc)
            )
        )
        :effect (and
            (at end (and
                    (hint_found ?hnt)
            ))
        )
    )
    

    (:durative-action reason
    :parameters (?hnt - hint ?hyp - hypothesis ?loc - location ?nav - navigation_token)
    :duration (= ?duration 1)
    :condition 
        (at start
            (and
                (at ?loc)
                (hint_found ?hnt )
            )
        )
    :effect 
        (at end 
            (and
                (not (hint_found ?hnt ))
                (consistent_hypothesis ?hyp)
                (proceed_investigate ?nav)
            )
        )
    )


    (:durative-action oracle
    :parameters (?from ?to - location ?hyp - hypothesis ?gm - game )
    :duration (= ?duration 1)
    :condition (and
        (at start
            (and
                (no_same_location ?from ?to)
                (at ?from)
                (is_oracle ?from)
                (consistent_hypothesis ?hyp)
            )
        )
    )
    :effect 
        (at end 
            (and
                (at ?to)
                (not (at ?from))
                (game_finished ?gm)
            )
        )
    )
)