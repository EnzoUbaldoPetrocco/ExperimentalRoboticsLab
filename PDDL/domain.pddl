(define (domain m2wr_cluedo)
    (:requirements :strips :typing :durative-actions :disjunctive-preconditions )
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
        (fnd_hint)

    )

    (:durative-action navigation
        :parameters (?from ?to - location ?nav - navigation_token  ?hnt - hint)
        :duration (= ?duration 1)
        :condition 
            (at start (and
                    (proceed_investigate ?nav)
                    ;(or 
                    (no_same_location ?from ?to)
                    ;(no_same_location ?to ?from)
                    ;)
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
                    (fnd_hint)
            ))
        )
    )


    (:durative-action find_hint
        :parameters (?loc - location ?hnt - hint)
        :duration (= ?duration 1)
        :condition 
            (at start (and
                    (at ?loc)
                    (fnd_hint)
            )
        )
        :effect (and
            (at end (and
                    (hint_found ?hnt)
                    (not (fnd_hint))
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
    :parameters (?loc - location ?hyp - hypothesis ?gm - game )
    :duration (= ?duration 1)
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