"""Explanations for the Mechanical Engineering specialism decks."""
from . import E

EXPLAIN = {
    "specialism/01-design-principles-methodologies-and-verification.pptx": {
        "Principles of engineering design": E(
            "Every design starts with requirements: function, aesthetics, dimensions, ergonomics, safety, "
            "sustainability, cost and materials.\n\n"
            "Requirements are found through market research, interviewing and observing the client, and analysing "
            "existing products. They're recorded in a design brief, a specification, questionnaires and observation "
            "records, then agreed with the client so the project scope is clear.\n\n"
            "Designs are communicated with orthographic drawings, virtual models and physical models. Factors such as "
            "the product life cycle, sustainability and safety shape every decision.",
            "A specification for a wheelbarrow: carry 100 kg, tip easily, handles 850 to 950 mm high, weigh under "
            "15 kg, cost under 60 pounds to make.",
            [("Name three ways to identify requirements.", "Market research, client interviews or observation, product analysis."),
             ("What is a specification?", "A detailed, measurable list of requirements."),
             ("Why agree the scope with the client?", "So everyone knows exactly what will be delivered.")]),
        "Design methodologies": E(
            "The systems approach designs the whole product and how its parts interact, suiting complex products "
            "such as gearboxes. The sub-assembly approach designs groups of parts as units, suiting modular products. "
            "Component-by-component design works on each part individually, suiting simple or bespoke items.\n\n"
            "Design for manufacture and assembly (DFM/DFA) makes parts easy and cheap to make and fit together, "
            "within the process's capability and tolerances.\n\n"
            "Planned obsolescence deliberately limits a product's life. Anthropometric tables help size products to people.",
            "DFA: designing a cover to snap-fit instead of using six screws cuts assembly time from two minutes to ten seconds.",
            [("Which methodology suits a gearbox?", "The systems approach."),
             ("What is DFA?", "Design for assembly: making parts easy to fit together."),
             ("What is planned obsolescence?", "Deliberately limiting a product's life.")]),
        "Verification and validation": E(
            "Verification asks 'did we build it right?'. It checks the design meets its specification, using "
            "comparison matrices, measurements and functional tests.\n\n"
            "Validation asks 'did we build the right thing?'. It checks the product meets the user's real needs, "
            "using user testing, ranking and decision trees.\n\n"
            "Both are needed at every stage: a part can meet every dimension on the drawing (verified) yet still be "
            "awkward to use (not validated).",
            "A handle is measured and matches the drawing (verified), but user tests show it hurts after ten minutes "
            "(not validated), so it's redesigned.",
            [("What question does verification answer?", "Did we build it right?"),
             ("What question does validation answer?", "Did we build the right thing?"),
             ("Give one validation method.", "E.g. user testing.")]),
    },
    "specialism/02-mechanical-drawings-standards-and-communication.pptx": {
        "Mechanical drawings": E(
            "Orthographic drawings show accurate views on standard sheet sizes. Section views show the inside of a "
            "part as if cut through, with the cut surfaces hatched.\n\n"
            "Standard features such as springs, splines, gears, webs, solid shafts, keys and keyways are drawn using "
            "simplified conventions, so they don't need drawing in full detail.\n\n"
            "Symbols such as balloons (numbering parts on an assembly), diameter and depth follow BS EN 8888, so any "
            "engineer can read the drawing the same way.",
            "A gearbox assembly drawing uses balloons to number each part, matching a parts list, and a section view "
            "shows the bearings inside.",
            [("What does a section view show?", "The inside of a part as if cut through."),
             ("What is a balloon on a drawing?", "A numbered label identifying a part."),
             ("Which standard covers drawing conventions?", "BS EN 8888.")]),
        "Communicating engineering information": E(
            "Engineering information is shared as CAD models and drawings, written specifications, SOPs and reports, "
            "presentations, graphs of test data and SPC, and CNC programs sent to machines.\n\n"
            "The audience decides the format: designers and manufacturing engineers need precise drawings and data; "
            "customers need clear visuals; non-technical staff need plain summaries.\n\n"
            "Digital tools help: 2D CAD for manufacturing drawings, 3D CAD for models and assemblies, CAE to simulate "
            "performance, and CAD to CAM transfer to send toolpaths to CNC machines.",
            "The same bracket: a toleranced drawing for the machinist, a rendered 3D image for the customer, and a "
            "one-paragraph cost summary for the manager.",
            [("What does CAE do?", "Simulates how a design will perform."),
             ("How do CNC machines get instructions from CAD?", "Through CAD to CAM transfer."),
             ("Why adapt the format to the audience?", "Each audience needs different detail and language.")]),
    },
    "specialism/03-simple-machines-and-mechanical-calculations.pptx": {
        "Simple machines": E(
            "Simple machines change the size, direction or type of motion.\n\n"
            "Gears transmit rotation: spur gears (parallel shafts), helical (quieter), bevel (turning through 90 "
            "degrees), worm (large reductions) and rack and pinion (rotary to linear).\n\n"
            "Levers are class 1 (pivot in the middle, like a seesaw), class 2 (load in the middle, like a wheelbarrow) "
            "or class 3 (effort in the middle, like tweezers).\n\n"
            "Linkages include reverse motion, parallel motion, bell crank and crank and slider. Cams (circular, "
            "eccentric, snail) turn rotation into reciprocating motion. Pulleys change the direction of force and "
            "ratchets allow movement one way only.",
            "A car's steering uses a rack and pinion to turn the steering wheel's rotation into the sideways motion "
            "that turns the wheels.",
            [("Which gear turns rotation into linear motion?", "Rack and pinion."),
             ("Which lever class is a wheelbarrow?", "Class 2."),
             ("What does a cam do?", "Turns rotary motion into reciprocating motion.")]),
        "Gear trains": E(
            "Gear ratio = teeth on the driven gear / teeth on the driver gear.\n\n"
            "Output speed = input speed / gear ratio. A ratio above 1 slows the output but increases torque; below 1 "
            "speeds it up and reduces torque.\n\n"
            "In a compound gear train, two gears share a shaft. Multiply the ratios of each pair to get the overall "
            "ratio, which allows large reductions in a small space.\n\n"
            "An idler gear between two gears changes the direction of rotation but not the ratio.",
            "Driver 20 teeth to driven 60 teeth (3:1), then on the same shaft 15 teeth to 45 teeth (3:1). Overall "
            "ratio = 3 x 3 = 9:1, so 900 rpm in gives 100 rpm out.",
            [("A 25-tooth driver meshes with a 75-tooth gear. Gear ratio?", "3:1."),
             ("If the input is 1,200 rpm through a 4:1 ratio, what is the output?", "300 rpm."),
             ("How do you find a compound train's ratio?", "Multiply the ratios of each pair.")]),
        "Machine performance": E(
            "Mechanical advantage (MA) = load / effort. It shows how much a machine multiplies force.\n\n"
            "Velocity ratio (VR) = distance moved by the effort / distance moved by the load. It depends only on the "
            "machine's geometry.\n\n"
            "Efficiency = MA / VR x 100%. Real machines are never 100% efficient because of friction and the weight of "
            "moving parts.\n\n"
            "Work = force x distance, and power = work / time.",
            "A pulley system lifts 800 N with 250 N effort. The effort moves 4 m while the load rises 1 m. MA = 3.2, "
            "VR = 4, efficiency = 80%.",
            [("What is the formula for mechanical advantage?", "Load / effort."),
             ("If MA is 3 and VR is 4, what is the efficiency?", "75%."),
             ("Why is efficiency never 100%?", "Friction and the weight of moving parts.")]),
    },
    "specialism/04-loads-environment-and-aerodynamics.pptx": {
        "Mechanical loads": E(
            "Loads can be static (steady, like a shelf's weight) or dynamic (changing, like a vibrating engine). "
            "A point load acts at one spot; a uniformly distributed load spreads evenly along a length.\n\n"
            "Torque twists; shear forces make layers slide; bending moments bend a member. Fluid loading comes from "
            "wind or water.\n\n"
            "Fatigue is the danger of dynamic loads: repeated cycles grow cracks until failure, even at loads well "
            "below the material's strength.\n\n"
            "The type of load decides which material properties matter most.",
            "A crane hook carries a static load when holding and a dynamic load when the load swings or is dropped "
            "suddenly, which can be far higher.",
            [("What is a uniformly distributed load?", "A load spread evenly along a length."),
             ("Why are dynamic loads a fatigue risk?", "Repeated cycles grow cracks."),
             ("What does a bending moment do?", "Bends a member.")]),
        "Aerodynamics": E(
            "Laminar flow moves in smooth, parallel layers. Turbulent flow is chaotic. Where flow can't follow a "
            "surface it separates, creating vortices behind the object.\n\n"
            "Lift acts at right angles to the flow, created by pressure differences. Drag opposes motion. Thrust "
            "drives an object forward. Turbulence creates fluctuating loads that can cause vibration and fatigue.\n\n"
            "Designers read 2D flow diagrams around shapes to predict these forces on structures such as masts, "
            "bridges, vehicles and wind turbines.",
            "Tall chimneys have a spiral strake that breaks up vortices, stopping wind making them oscillate.",
            [("What is a separation point?", "Where flow leaves the surface."),
             ("What direction does lift act?", "At right angles to the flow."),
             ("Why can turbulence damage structures?", "Fluctuating loads cause vibration and fatigue.")]),
    },
    "specialism/05-business-context-constraints-and-metrics.pptx": {
        "Context": E(
            "Market pull happens when customers create demand and designers respond to a known need, such as a "
            "lighter cordless drill.\n\n"
            "Technology push happens when a new technology creates an opportunity and designers find a market for "
            "it, such as early 3D printers.\n\n"
            "Context also includes commercial advantage, designing for reuse, planned obsolescence and "
            "sustainability. Constraints come from commercial factors (competition, profit), operational factors "
            "(tools, materials, process capability, skills), legal requirements and design for manufacture.",
            "Customers wanted longer battery life (market pull); lithium-ion technology made it possible (technology push).",
            [("What is market pull?", "Products developed in response to customer demand."),
             ("What is technology push?", "New technology creating products that find a market."),
             ("Give an operational constraint.", "E.g. tools, materials, process capability, skills.")]),
        "Cost and profit": E(
            "Manufacturing cost per unit = materials + labour + overheads.\n\n"
            "Materials are the raw stock and bought-in parts. Labour is the workers' time. Overheads are the "
            "running costs of the business (rent, energy, admin) shared across the products.\n\n"
            "Profit per unit = selling price - manufacturing cost.\n\n"
            "Design decisions, such as choice of material, number of parts and process, drive most of a product's "
            "cost, so commercial risk analysis is part of every design review.",
            "Materials 3 pounds + labour 4.50 + overheads 2.50 = 10 pounds. Selling at 14 pounds gives 4 pounds "
            "profit, a 40% margin on cost.",
            [("Name the three parts of manufacturing cost.", "Materials, labour, overheads."),
             ("Cost 12 pounds, price 15 pounds. Profit per unit?", "3 pounds."),
             ("Why do design decisions affect cost so much?", "They set materials, parts and processes.")]),
    },
    "specialism/06-materials-standard-parts-and-processes.pptx": {
        "Choosing materials": E(
            "Choose materials for fitness for purpose (the properties the function needs), availability (standard "
            "stock sizes and lead times), risk (the consequences if it fails) and a factor of safety.\n\n"
            "A factor of safety designs a part to be stronger than the expected load. A factor of 2 means it could "
            "carry twice the working load. Higher factors are used where failure would be dangerous or loads are uncertain.\n\n"
            "Material families range from ferrous and non-ferrous metals to thermoplastics, thermosets, elastomers, "
            "composites, ceramics and smart materials.",
            "A lifting hook rated for 1 tonne with a factor of safety of 5 is designed not to fail below 5 tonnes.",
            [("What is a factor of safety?", "Designing a part stronger than its expected load."),
             ("When would you use a higher factor of safety?", "When failure is dangerous or loads are uncertain."),
             ("Name two considerations when choosing a material.", "E.g. fitness for purpose, availability, risk.")]),
        "Manufacturing processes": E(
            "Wasting processes (cutting, filing, turning, milling, grinding) remove material. They're accurate but "
            "waste material. Shaping (casting, moulding) makes complex shapes but tooling is expensive. Forming "
            "(bending, pressing) is fast with little waste but needs ductile material.\n\n"
            "Welding makes strong, permanent joints: MIG/MAG is fast for general work; TIG is slower but neat and "
            "precise, for thin or stainless material. Heat can distort parts. 3D printing makes complex one-offs but "
            "is slow in volume. Joining, finishing and assembly complete the product.\n\n"
            "Tolerances and fits must be designed so parts assemble correctly.",
            "10,000 plastic clips: injection moulding (shaping). One prototype clip: 3D printing.",
            [("Which welding process gives the neatest finish on thin stainless steel?", "TIG."),
             ("Why is casting costly for small quantities?", "Tooling is expensive."),
             ("What does forming need from the material?", "Ductility.")]),
    },
    "specialism/07-quality-testing-and-measurement.pptx": {
        "Causes of error": E(
            "Assignable (systematic) causes have an identifiable reason: faulty calibration, tool wear, observer bias "
            "or human error. They push results consistently one way and can be found and fixed.\n\n"
            "Random causes come from ambient conditions such as temperature and humidity, and instrument uncertainty. "
            "They scatter results unpredictably and can be reduced but never eliminated.\n\n"
            "Quality assurance prevents errors through procedures, calibration, process capability monitoring and "
            "preventative maintenance. Quality control catches them through testing and inspection. High volumes "
            "suit sampling; critical or low-volume parts may need 100% inspection.",
            "Every shaft measures 0.05 mm oversize: a systematic error, probably worn tooling or a misset machine. "
            "Readings scattered either side point to random error.",
            [("Is tool wear an assignable or random cause?", "Assignable."),
             ("Can random error be eliminated?", "No, only reduced."),
             ("When is 100% inspection used?", "For critical or low-volume parts.")]),
        "Testing methods": E(
            "Non-destructive testing (NDT) checks parts without damaging them. Visual inspection, measurement and "
            "go/no-go gauges find surface and size faults. Penetrant testing and magnetic particle inspection reveal "
            "surface cracks. Ultrasonic testing and X-radiography find flaws inside.\n\n"
            "Destructive testing sacrifices a sample: tensile tests (strength), hardness tests, impact tests such as "
            "Izod and Charpy (toughness) and macro examination (internal structure).\n\n"
            "NDT can check every part; destructive tests check samples from a batch.",
            "Every weld on a pressure vessel is X-rayed (NDT), while sample welds from the same batch are cut and "
            "tensile tested (destructive).",
            [("Which NDT method finds internal flaws?", "Ultrasonic or X-radiography."),
             ("What does a Charpy test measure?", "Toughness (impact energy absorbed)."),
             ("Why can't destructive testing check every part?", "The part is destroyed.")]),
        "Measurement equipment": E(
            "Choose equipment by what's being measured and how accurately.\n\n"
            "Rules and protractors for basic length and angle. Vernier and digital callipers for inside, outside and "
            "depth. Micrometers for precise small dimensions. Gauges: go/no-go for quick pass or fail, slip gauges as "
            "precise reference lengths, plug gauges for holes. Dial test indicators for run-out. CMMs and laser "
            "scanning for complex 3D shapes. Digital stress and strain machines for mechanical properties.\n\n"
            "Analyse readings statistically: mean, range and standard deviation show whether a process is in tolerance.",
            "Ten shafts measure 20.01, 20.02, 20.00... The mean of 20.01 mm and a small standard deviation show the "
            "process is centred and consistent.",
            [("What is a go/no-go gauge for?", "A quick pass or fail check."),
             ("What is a slip gauge?", "A precise reference length."),
             ("What does a large standard deviation show?", "Readings vary a lot, so the process is inconsistent.")]),
    },
    "specialism/08-installation-and-integration.pptx": {
        "Installation requirements": E(
            "Installing a mechanical system must satisfy three sets of requirements.\n\n"
            "Customer requirements: what the system must do on site, where it goes and how it will be used. "
            "Regulatory requirements: safety law and standards, such as PUWER and machinery safety rules. "
            "Manufacturer specifications: foundations, mounting, alignment, torque settings, clearances and "
            "connections.\n\n"
            "Ignoring the manufacturer's specification can void the warranty and cause early failure.",
            "A pump installed with its shaft misaligned by half a millimetre will wear out its bearings and seals "
            "far faster than the manufacturer's rated life.",
            [("Name the three sources of installation requirements.", "Customer, regulatory, manufacturer."),
             ("Why follow the manufacturer's torque settings?", "To avoid damage or loosening and keep the warranty."),
             ("Which regulations cover work equipment safety?", "PUWER.")]),
        "Integrating systems": E(
            "Integration brings separate sub-systems together into one working system.\n\n"
            "Plan the interfaces (where sub-systems connect) and the sequence. Combine the sub-systems. Connect their "
            "functions: mechanical links, electrical supplies and control signals. Test each interface, then the "
            "whole system. Finally commission it to prove it works as specified.\n\n"
            "Testing interfaces one at a time makes faults much easier to find than switching everything on at once.",
            "A packaging line: the conveyor, sensor system and robotic arm are each tested, then linked one at a time, "
            "then run together at slow speed before full production.",
            [("What is an interface?", "A point where two sub-systems connect."),
             ("Why test interfaces one at a time?", "Faults are easier to find."),
             ("What is the final stage of integration?", "Commissioning.")]),
    },
    "specialism/09-analysing-requirements-and-design-information.pptx": {
        "Scope creep and design change": E(
            "Scope creep is when a project's requirements grow bit by bit without being properly agreed: 'just one "
            "more feature'. Each change adds cost and time, and together they can wreck a schedule or budget.\n\n"
            "Process-driven change happens when manufacturing limits force a redesign, such as a tolerance the "
            "machines can't hold.\n\n"
            "Manage both by recording every change, assessing its impact on cost, time and risk, getting it agreed, "
            "and escalating anything that affects the original brief.",
            "A client asks for a bracket to also hold a cable tidy. Logged as a change, it adds two days and 300 "
            "pounds, and the client agrees before work starts.",
            [("What is scope creep?", "Uncontrolled growth in requirements."),
             ("What is process-driven change?", "A redesign forced by manufacturing limits."),
             ("What should happen to every change?", "It's recorded, assessed and agreed.")]),
        "Verifying design information": E(
            "Before a design goes further, check it actually meets the requirements: the components, materials, "
            "application, location, risks and environment.\n\n"
            "Use technology to evaluate it: mathematical calculations to check loads and stresses, CAD simulations "
            "to test the design virtually, and physical models to check fit, form and function.\n\n"
            "Using more than one method gives confidence, because each can catch mistakes the others miss.",
            "A CAD stress simulation shows a bracket is safe, but a hand calculation disagrees by a factor of ten: "
            "the load had been entered in the wrong units.",
            [("Name three ways to evaluate a design.", "Calculations, CAD simulation, physical models."),
             ("Why use more than one method?", "Each can catch mistakes the others miss."),
             ("What does a physical model check?", "Fit, form and function.")]),
    },
    "specialism/10-evaluating-and-improving-designs.pptx": {
        "Modelling and analysis": E(
            "Designs are modelled with mathematical models, spreadsheets and CAD simulations to predict performance "
            "and failure modes.\n\n"
            "Choose the tool by cost, availability, compatibility with other systems, training needs, time and "
            "which failure modes you need to check.\n\n"
            "Factors affecting a design include materials, application, location, risk, environment, configuration, "
            "geometry and scale. Designers also decide whether to optimise an existing design or develop a new one.",
            "A spreadsheet quickly compares beam sizes; a CAD simulation then checks the chosen beam's stress "
            "concentrations around bolt holes.",
            [("Name three factors when choosing a modelling tool.", "E.g. cost, availability, training, time."),
             ("What is the difference between optimising and developing a design?", "Optimising improves an existing design; developing creates a new one."),
             ("What is a failure mode?", "A way a design could fail.")]),
        "Evaluating and improving": E(
            "Designs are evaluated against their purpose, working conditions and application requirements such as "
            "cost and value. Value engineering improves value by cutting cost without losing function.\n\n"
            "Options are compared using fitness for purpose, context, constraints, agreed metrics and specification "
            "compliance, often in a weighted comparison matrix.\n\n"
            "Individual, team and organisational performance is reviewed against KPIs, and feedback and changes are "
            "handled constructively and logged.",
            "Three hinge designs are scored on strength, cost, weight and ease of assembly in a weighted matrix. The "
            "cheapest wins once strength is confirmed.",
            [("What is value engineering?", "Cutting cost without losing function."),
             ("What is a weighted comparison matrix?", "Scoring options against criteria that have different importance."),
             ("Why log design changes?", "For traceability.")]),
    },
    "specialism/11-designing-modelling-and-prototyping.pptx": {
        "From ideas to designs": E(
            "Designs develop from sketches into detailed, annotated concepts that show how each requirement is met "
            "and why materials were chosen.\n\n"
            "Mechanical systems are modelled and their performance calculated: linear systems such as levers and "
            "linkages, rotating systems such as gears and flywheels, and lifting machines such as cranes and pulleys, "
            "including dynamic effects from acceleration.\n\n"
            "CAD produces 2D and 3D drawings, simulations and accurate assemblies. Detailed drawings follow BS and ISO "
            "standards for accuracy, tolerances, units, scale and symbols.",
            "A crane design is sketched, its lifting performance calculated, modelled in 3D CAD with a clash check, "
            "and detailed for manufacture.",
            [("Why annotate concept sketches?", "To show how requirements are met and justify choices."),
             ("Give an example of a rotating system.", "E.g. gears or flywheels."),
             ("What standards do detailed drawings follow?", "BS and ISO.")]),
        "Tools, assembly and realisation": E(
            "Hand and power tools must be chosen correctly and used safely, with checks before, during and after "
            "use: guards fitted, cables and blades undamaged, calibration current, and damage reported.\n\n"
            "Prototyping must use at least one type of welding and one type of 3D printing.\n\n"
            "Assembly follows a sequence: aligning, fixing, jointing, pre-tensioning, sealing and tightening in order, "
            "then functional testing. Disassembly starts by safely releasing tension and pressure.\n\n"
            "A realisable design can actually be manufactured, operated and maintained.",
            "Bolts on a flange are tightened in a star pattern, a little at a time, so the joint seals evenly "
            "instead of warping.",
            [("Name two pre-use checks on a power tool.", "E.g. guards fitted, cable undamaged, correct blade."),
             ("Why release tension before disassembly?", "Stored energy could cause injury."),
             ("What makes a design realisable?", "It can be manufactured, operated and maintained.")]),
    },
    "specialism/12-collaboration-risk-and-quality-assurance.pptx": {
        "Risk management": E(
            "Engineers carry out risk management for their work, especially in machining, mechanical handling and "
            "high-power applications, identifying hazards and putting mitigation in place.\n\n"
            "In unfamiliar situations, the right response is to stop, assess the risk and seek advice rather than "
            "carry on.\n\n"
            "Commercial risks, such as missing a deadline or a supplier failing, are ranked using models that "
            "combine likelihood and impact, so the biggest are tackled first.",
            "Testing a new high-speed spindle: guard it, run it up in stages from outside the enclosure, and have "
            "an emergency stop within reach.",
            [("Name two high-risk engineering activities.", "E.g. machining, mechanical handling, high-power work."),
             ("What should you do in an unfamiliar risky situation?", "Stop, assess and seek advice."),
             ("How are commercial risks ranked?", "By combining likelihood and impact.")]),
        "Testing and quality assuring": E(
            "Models and prototypes, virtual or physical (block models, 3D prints, one-off prototypes), are tested "
            "through concept testing, functional tests, measurement and visual inspection. Results are recorded and "
            "acted on.\n\n"
            "Design information, such as proposals, specifications and drawings, is produced and quality assured to "
            "professional standards from bodies such as the Engineering Council, IMechE and IET.\n\n"
            "Completed drawings are checked for quality, technical compliance and completeness before release.",
            "A drawing checker spots a missing tolerance on a bearing bore before release, avoiding a batch of "
            "unusable parts.",
            [("Name two ways to test a prototype.", "E.g. functional tests, measurement, visual inspection."),
             ("What is a drawing checked for?", "Quality, technical compliance and completeness."),
             ("Name a professional engineering body.", "E.g. Engineering Council, IMechE, IET.")]),
    },
    "specialism/13-technical-documentation-and-communication.pptx": {
        "Managing documentation": E(
            "Technical documents, such as specifications and drawings, are produced, amended, checked and managed "
            "with digital tools: CAD, document management systems, SharePoint and spreadsheets.\n\n"
            "Version control keeps one current version: revision letters, change notes and a record of what changed "
            "and why. Everyone must work from the latest issue.\n\n"
            "Drawings are annotated with geometrical tolerances, limits and fits, and surface finishes, so the part "
            "can be made correctly.",
            "Two teams working from revision B and revision C of the same drawing make parts that don't fit: version "
            "control prevents this.",
            [("What is a revision letter for?", "Showing which version of a drawing is current."),
             ("Name two digital tools for managing documents.", "E.g. CAD, document management systems, SharePoint."),
             ("What is a surface finish annotation for?", "Specifying how smooth a surface must be.")]),
        "Communicating design information": E(
            "Design information includes specifications, proposals, working drawings, representations, data, "
            "processes, risks and outcomes.\n\n"
            "It's shared with stakeholders, colleagues and clients using sketches, schemes, detailed drawings, "
            "diagrams, models and reports.\n\n"
            "Choose the format by cost, time, availability, the end user and the scale of the project, and make "
            "each stage of the design process clear.",
            "A client meeting uses a 3D-printed model and a rendering; the workshop gets detailed drawings; the "
            "board gets a two-page report.",
            [("Name three formats for communicating design information.", "E.g. sketches, drawings, models, reports."),
             ("What decides the format?", "Cost, time, availability, end user, project scale."),
             ("Why show each stage of the design process?", "So others can follow and trust the decisions.")]),
    },
}
