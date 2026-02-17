from injector import (
    EngineInputs, PropellantInputs, FeedSystemInputs,
    InjectorFactory,
    ImpingingDesign, PintleDesign, CoaxDesign
)


def main() -> None:
    engine = EngineInputs(Pc=2.16e6, Dc=0.105, mdot_total=4.86, MR_target=2.0)
    prop = PropellantInputs(rho_o=1141.0, rho_f=800.0, mu_o=6.93e-5, mu_f=2.71e-3)
    feed = FeedSystemInputs(dP_o=4.32e5, dP_f=4.32e5)

    cases = [
        ("impinging", ImpingingDesign()),
        ("pintle", PintleDesign()),
        ("coax", CoaxDesign()),
    ]

    for injector_type, design in cases:
        print("\n" + "=" * 60)
        inj = InjectorFactory.create(injector_type, engine, prop, feed, design)
        result = inj.run()
        print("[run_demo] Result:", result)


if __name__ == "__main__":
    main()
