(define (domain m2wr_cluedo)
    (:requirements :strips ::durative-actions)
    (:types
        location
        hint
        hypothesis
        response
        navigation_token
    )
    (:predicates
        (hint_found ?hnt - hint)
        (consistent_hypothesis ?hyp - hypothesis)
        (oracle_res ?res - response)
        (is_oracle ?loc - location)
        (proceed_investigate ?nav - navigation_token)
        (no_same_location ?from ?to - location)
    )

    (:action navigation
    :parameters (?nav - navigation ?from ?to- location)
    :precondition (and
        (proceed_investigate ?nav - navigation_token)
        (no_same_location ?from ?to - location)
        (?from - location)
        )
    :effect (and
        (not (proceed_investigate ?nav - navigation_token))
        (hint_found ?hnt - hint)
        (?to - location)
        (not (?from - location))
        )
    )

    (:action reason
    :parameters (?hnt - hint)
    :precondition (
        (hint_found ?hnt - hint)
        )
    :effect (and
        (not (hint_found ?hnt - hint))
        (consistent_hypothesis ?hyp)
        )
    )


    (:action oracle
    :parameters (?from ?to - location ?hyp - hypothesis)
    :precondition (
        (no_same_location ?from ?to - location)
        (?from - location)
        (is_oracle ?loc - location)
        )
    :effect (and
        (not (hint_found ?hnt - hint))
        (consistent_hypothesis ?hyp- hypothesis)
        (?to - location)
        (not (?from - location))
        )
    )
)