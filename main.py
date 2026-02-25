from injector import (
    EngineInputs, PropellantInputs, FeedSystemInputs,
    ImpingingDesign, PintleDesign, CoaxDesign, 
    ImpingingInjector, PintleInjector, CoaxInjector
)


def main() -> None:
    engine = EngineInputs
    prop = PropellantInputs
    feed = FeedSystemInputs
    impDesign = ImpingingDesign
    
    print("\n" + "=" * 60, "\n")
    impinging = ImpingingInjector(engine, prop, feed, impDesign)
    impinging.run()
    print("\n" + "=" * 60, "\n")


if __name__ == "__main__":
    main()
