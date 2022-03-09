(define (domain m2wr_cluedo)
    (:requirements :strips :typing :durative-actions )
    (:types
        location
        hint
        hypothesis
        navigation_token
        game
    )
    (:predicates
        (at ?loc - location)
        (not_at ?loc - location)
        (hint_found ?hnt - hint)
        (consistent_hypothesis ?hyp - hypothesis)
        (is_oracle ?loc - location)
        (proceed_investigate ?nav - navigation_token)
        (no_same_location ?from ?to - location)
        (game_finished ?gm - game)

    )

    (:durative-action navigation
        :parameters (?nav - navigation_token ?from ?to - location ?hnt - hint)
        :duration (= ?duration 0.001)
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
                    (not_at ?from)
                    (not (at ?from))
                    (not (not_at ?to))
            ))
        )
    )


    (:durative-action find_hint
        :parameters (?nav - navigation_token ?loc - location ?hnt - hint)
        :duration (= ?duration 0.001)
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
    :duration (= ?duration 0.001)
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
    :parameters (?loc - location ?hyp - hypothesis ?gm - game )
    :duration (= ?duration 0.001)
    :condition (and
        (at start
            (and
                (is_oracle ?loc)
                (consistent_hypothesis ?hyp)
            )
        )
    )
    :effect 
        (at end 
            (and
                (not (consistent_hypothesis ?hyp))
                (game_finished ?gm)
            )
        )
    )
)