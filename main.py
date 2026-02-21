from injector import (
    EngineInputs, PropellantInputs, FeedSystemInputs,
    InjectorFactory,
    ImpingingDesign, PintleDesign, CoaxDesign
)


def main() -> None:
    engine = EngineInputs
    prop = PropellantInputs
    feed = FeedSystemInputs

    cases = [
        ("impinging", ImpingingDesign()),
        # ("pintle", PintleDesign()),
        # ("coax", CoaxDesign()),
    ]

    for injector_type, design in cases:
        print("\n" + "=" * 60, "\n")
        inj = InjectorFactory.create(injector_type, engine, prop, feed, design)
        result = inj.run()
        print("\n" + "=" * 60, "\n")
        # print("Result:", result, "\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
