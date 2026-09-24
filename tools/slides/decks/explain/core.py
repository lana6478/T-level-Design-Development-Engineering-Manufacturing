"""Explanations for the Engineering Core decks."""
from . import E

EXPLAIN = {
    "core/01-design-principles-and-manufacturing-approaches.pptx": {
        "Types of manufacturing process": E(
            "Manufacturing processes are grouped by how they change material.\n\n"
            "Wasting removes material to leave the shape you want: cutting, drilling, turning and milling. It's "
            "accurate but creates waste. Forming bends or presses material without removing any. Shaping and casting "
            "pour or push material into a mould. Joining connects parts by welding, brazing, fixings or adhesives. "
            "Finishing protects or improves the surface. Additive manufacturing, such as 3D printing, builds a part "
            "layer by layer, so complex shapes are possible with little waste.\n\n"
            "The process chosen affects cost, quantity, accuracy, strength and appearance.",
            "A steel bracket could be milled from a solid block (wasting), laser cut then bent (forming), or 3D "
            "printed in metal (additive). Bending sheet is cheapest in volume.",
            [("Which process type removes material?", "Wasting."),
             ("Why is additive manufacturing good for complex shapes?", "It builds parts layer by layer."),
             ("Name two joining methods.", "E.g. welding, brazing, fixings, adhesives.")]),
        "Approaches to design": E(
            "Linear design moves through fixed stages in order: brief, research, specification, ideas, development, "
            "manufacture and evaluation. It's easy to manage but slow to react to problems.\n\n"
            "Iterative design cycles through design, test, evaluate and improve, repeatedly. Test results feed each "
            "new version, so problems are found early.\n\n"
            "Other approaches include inclusive and user-centred design (designing around real users), design for "
            "manufacture and assembly (making parts easy to make and fit together), and sustainable design, guided by "
            "the 6Rs: reduce, refuse, rethink, repair, reuse and recycle.\n\n"
            "Anthropometric data, body measurements, makes products fit people.",
            "Designing a drill handle: anthropometric data sets the grip size; three 3D-printed iterations are tested "
            "with users before the final design.",
            [("What is the key difference between linear and iterative design?", "Iterative repeats test and improve cycles; linear goes through stages once."),
             ("Name three of the 6Rs.", "Any three: reduce, refuse, rethink, repair, reuse, recycle."),
             ("What is anthropometric data?", "Measurements of the human body, used for ergonomic design.")]),
        "Scale of manufacture": E(
            "How many products are made shapes how they're made.\n\n"
            "One-off: a single bespoke item, made by skilled workers or with computer-aided manufacture (CAM). "
            "Batch: a set quantity, then the equipment is changed over for the next product. Mass: very large "
            "numbers on dedicated, highly automated production lines. Continuous: production runs non-stop, such as "
            "steel sheet or chemicals.\n\n"
            "Higher volumes justify more automation and investment in tooling, lowering the cost of each item. "
            "Factories can be laid out by function, by product, as a matrix, or in cells.",
            "A racing car wing is one-off; a run of 500 brackets is batch; car door handles are mass produced; "
            "petrol is refined continuously.",
            [("Which scale suits bespoke items?", "One-off."),
             ("Why does mass production use more automation?", "High volumes justify the investment and lower unit cost."),
             ("Give an example of continuous production.", "E.g. steel sheet, chemicals, petrol.")]),
    },
    "core/02-maintenance-repair-and-installation.pptx": {
        "Types of maintenance": E(
            "Planned maintenance is scheduled in advance, such as servicing a machine every 500 hours. It's "
            "predictable but may replace parts that still had life left.\n\n"
            "Reactive maintenance fixes things when they break. There's no upfront cost, but breakdowns are "
            "unplanned and can stop production.\n\n"
            "Preventative maintenance carries out regular checks and servicing to stop failures happening.\n\n"
            "Condition-based monitoring uses sensors, such as for vibration or temperature, to spot early signs of "
            "wear, so work is done only when needed. It's efficient but needs sensors and data analysis.",
            "A vibration sensor on a pump shows a rising trend. The bearing is replaced at the next planned stop, "
            "before it fails mid-shift.",
            [("Which maintenance type waits for a breakdown?", "Reactive."),
             ("What does condition-based monitoring use?", "Sensor data, e.g. vibration or temperature."),
             ("Give one drawback of planned maintenance.", "Parts may be replaced before they need to be.")]),
        "Installation and the future of maintenance": E(
            "New equipment must be installed to meet customer requirements, regulations and the manufacturer's "
            "specifications. Commissioning then checks it works safely and as intended before it goes into use.\n\n"
            "Maintenance roles include the machine operator (who runs it and reports faults), the maintenance "
            "engineer (who services and repairs it) and the maintenance manager (who plans the work).\n\n"
            "New technology, such as sensors, data and predictive software, is making maintenance smarter. Good "
            "maintenance also helps the environment: efficient machines use less energy, last longer and create less waste.",
            "A new CNC machine is levelled and wired to the manufacturer's specification, then commissioned by "
            "running test parts and checking the dimensions before production starts.",
            [("What is commissioning?", "Checking new equipment works safely and as intended before use."),
             ("Who plans maintenance work?", "The maintenance manager."),
             ("How does maintenance help the environment?", "Efficient machines use less energy and create less waste.")]),
    },
    "core/03-engineering-past-present-and-future.pptx": {
        "Historical advances": E(
            "Engineering has transformed how people live.\n\n"
            "New materials, such as steel, made stronger structures possible. Electrical power and lighting "
            "transformed factories and homes. The internal combustion engine and electric motors made modern "
            "transport and machinery possible. Replaceable parts and mass production made goods cheap and repairable. "
            "Radio, television, computers and the internet changed communication and allowed automation.\n\n"
            "These advances reshaped transport, healthcare, housing and employment, and now drive the push for "
            "sustainability.",
            "Replaceable, standardised parts meant a broken rifle or car could be repaired with a new part instead "
            "of being hand-made again: the basis of mass production.",
            [("Why were replaceable parts important?", "They enabled mass production and easy repair."),
             ("Name two advances that changed transport.", "E.g. internal combustion engine, electric motor."),
             ("How did computers change manufacturing?", "They enabled automation and precise control.")]),
        "Emerging trends": E(
            "Several trends are reshaping engineering.\n\n"
            "Digitalisation, the Internet of Things and cloud computing connect machines and data. Cyber-physical "
            "systems tightly link physical equipment with software control. AI analyses data and optimises processes. "
            "Robotics, drones and autonomous systems take on repetitive or dangerous work. Virtual and augmented "
            "reality help with design and training. Distributed energy and hybrid technologies change how power is "
            "made and used. The circular economy keeps materials in use through reuse, repair and recycling.",
            "A 'smart factory' uses IoT sensors on every machine, AI to predict breakdowns, and robots for assembly, "
            "all monitored from the cloud.",
            [("What is a cyber-physical system?", "Physical equipment tightly controlled by software and networks."),
             ("What is the circular economy?", "Keeping materials in use through reuse, repair and recycling."),
             ("How can AR help engineers?", "E.g. overlaying instructions for training and maintenance.")]),
    },
    "core/04-engineering-drawings-and-tolerancing.pptx": {
        "Drawing types": E(
            "Engineers choose a drawing type to suit its purpose and audience.\n\n"
            "Freehand sketches capture ideas quickly. Isometric drawings show an object in 3D at a fixed angle, "
            "easy for anyone to understand. Orthographic projection shows accurate 2D views (front, side and plan) "
            "with dimensions, used for manufacture. Exploded views show how parts fit together. CAD models are "
            "accurate 3D models that can be tested virtually. Block diagrams, flowcharts, circuit diagrams and "
            "schematics show systems.\n\n"
            "Drawings follow standards such as BS EN 8888 for technical drawings and BS 3939 for graphical symbols.",
            "A customer sees an isometric rendering; the machinist works from an orthographic drawing; the assembly "
            "team uses an exploded view.",
            [("Which drawing type is used for manufacture?", "Orthographic projection."),
             ("What does an exploded view show?", "How parts assemble."),
             ("Which standard covers technical drawings?", "BS EN 8888.")]),
        "Tolerances, limits and fits": E(
            "No part can be made to an exact size, so drawings state how much variation is acceptable.\n\n"
            "The tolerance is the total allowed variation. The limits are the largest and smallest acceptable sizes. "
            "A dimension of 20 mm plus or minus 0.1 mm has limits of 19.9 mm and 20.1 mm and a tolerance of 0.2 mm.\n\n"
            "Fits describe how two parts go together. A clearance fit always leaves a gap, so parts move freely. An "
            "interference fit is always tight, so parts must be pressed together. A transition fit could be either.\n\n"
            "Tighter tolerances cost more, so specify only what the function needs.",
            "A shaft is 25.00 to 25.02 mm and its hole 25.05 to 25.08 mm. The smallest gap is 0.03 mm, so it's a "
            "clearance fit and the shaft always turns freely.",
            [("A dimension is 50 mm plus or minus 0.2 mm. What are the limits?", "49.8 mm and 50.2 mm."),
             ("Which fit always needs pressing together?", "An interference fit."),
             ("Why not make every tolerance tight?", "Tighter tolerances cost more to make.")]),
        "Geometric tolerancing (GD&T)": E(
            "Size tolerances aren't always enough: a hole can be the right size but in the wrong place or at the "
            "wrong angle. Geometric dimensioning and tolerancing (GD&T) controls form, orientation and position.\n\n"
            "A datum is a reference surface or feature everything is measured from. Parallelism keeps a surface "
            "parallel to a datum. Perpendicularity keeps it at 90 degrees. Concentricity keeps circular features on "
            "the same centre. Straightness keeps a line or edge straight.\n\n"
            "Each has a standard symbol in a feature control frame on the drawing.",
            "A bearing bore must be concentric with the shaft centre line within 0.02 mm, or the shaft will wobble "
            "and wear the bearing.",
            [("What is a datum?", "A reference feature that other features are measured from."),
             ("What does concentricity control?", "That circular features share the same centre."),
             ("Why isn't size tolerance always enough?", "A feature can be the right size but wrongly positioned or angled.")]),
    },
    "core/05-essential-mathematics.pptx": {
        "The maths toolkit": E(
            "Engineers use maths every day to design, check and make things.\n\n"
            "Arithmetic: standard form for very large or small numbers, fractions, percentages, ratios and BIDMAS "
            "(the order of operations). Algebra: rearranging formulae, solving simultaneous and quadratic equations, "
            "indices, logarithms, sequences and matrices. Geometry: areas and volumes. Calculus: straight-line graphs "
            "(y = mx + c), differentiation to find maximum and minimum values, and integration. Trigonometry: "
            "Pythagoras, sine and cosine rules, radians and vectors. Statistics: averages, range, standard deviation "
            "and probability.",
            "Working out how much steel is needed for 200 cylindrical pins uses geometry (volume), arithmetic "
            "(multiplying up) and percentages (adding waste).",
            [("What does BIDMAS tell you?", "The order to carry out operations."),
             ("What is y = mx + c?", "The equation of a straight line (m is gradient, c is intercept)."),
             ("What is differentiation used for?", "E.g. finding maximum and minimum values.")]),
        "Worked examples": E(
            "Standard form: 0.00045 m is written 4.5 x 10 to the power -4 m, so the size is clear at a glance.\n\n"
            "Straight lines: a line through (0, 2) with a gradient of 3 is y = 3x + 2.\n\n"
            "Volume: a cylinder's volume is pi x r squared x h. With r = 0.1 m and h = 2 m, that's about 0.063 cubic metres.\n\n"
            "Triangles: Pythagoras (a squared + b squared = c squared) works for right-angled triangles; the sine "
            "rule (a / sin A = b / sin B) and cosine rule handle any triangle.\n\n"
            "Always write the formula, substitute with units, then round sensibly.",
            "A 5 m ladder with its foot 3 m from a wall: height = square root of (25 - 9) = square root of 16 = 4 m.",
            [("Write 0.0072 in standard form.", "7.2 x 10 to the power -3."),
             ("What is the volume formula for a cylinder?", "pi x r squared x h."),
             ("When can you use Pythagoras?", "In right-angled triangles.")]),
        "Number systems": E(
            "Decimal (base 10) is used every day. Binary (base 2) uses only 0 and 1, matching the on and off states "
            "of digital electronics, so PLCs, sensors and control systems work in binary. Hexadecimal (base 16) uses "
            "0 to 9 and A to F; each hex digit stands for four binary digits, so it's a compact way to write binary, "
            "used for memory addresses and machine codes.\n\n"
            "To convert binary to decimal, add the place values of the 1s: 8, 4, 2, 1 from the left for four bits.",
            "Binary 1011 = 8 + 0 + 2 + 1 = 11 in decimal, which is B in hexadecimal.",
            [("Convert binary 1100 to decimal.", "12."),
             ("Why do digital systems use binary?", "It matches on and off electrical states."),
             ("How many binary digits does one hex digit represent?", "Four.")]),
    },
    "core/06-units-measurement-and-scientific-method.pptx": {
        "Units": E(
            "SI base units include the metre (length), kilogram (mass) and second (time). Derived units combine "
            "them: the newton (N) for force, the pascal (Pa, newtons per square metre) for pressure, the newton "
            "metre for torque, metres per second for velocity and kilograms per cubic metre for density.\n\n"
            "Prefixes scale units from tera (10 to the power 12) to pico (10 to the power -12). Common ones: kilo (1,000), "
            "mega (1,000,000), milli (0.001) and micro (0.000001).\n\n"
            "Some industries still use imperial units, such as the inch (25.4 mm) and foot, so conversions matter.",
            "A pressure of 2.5 MPa is 2,500,000 Pa. A 2 inch pipe is 50.8 mm.",
            [("What is the SI unit of force?", "The newton (N)."),
             ("How many pascals in 1 kPa?", "1,000."),
             ("Convert 4 inches to millimetres.", "101.6 mm.")]),
        "Vectors and coordinates": E(
            "A scalar has size only, such as distance, speed or mass. A vector has size and direction, such as "
            "displacement, velocity, acceleration or force. Walking 5 km is a distance; walking 5 km north is a "
            "displacement.\n\n"
            "Positions can be described with Cartesian coordinates (x, y) or polar coordinates (a distance r and an "
            "angle). To convert polar to Cartesian: x = r cos angle, y = r sin angle. To convert back: "
            "r = square root of (x squared + y squared).\n\n"
            "CNC machines and robots use both systems to position tools.",
            "A robot arm reaches 0.5 m at 30 degrees: x = 0.5 cos 30 = 0.43 m, y = 0.5 sin 30 = 0.25 m.",
            [("Is speed a scalar or a vector?", "A scalar."),
             ("How do you convert polar to Cartesian x?", "x = r cos angle."),
             ("Give an example of a vector.", "E.g. velocity, displacement, force.")]),
        "The scientific method": E(
            "Engineers test ideas scientifically rather than guessing.\n\n"
            "Observe something, ask a question, form a hypothesis (a testable explanation), make a prediction or run "
            "a simulation, carry out a fair test, and draw a conclusion. Then iterate: refine the hypothesis and test again.\n\n"
            "Judge results by accuracy (how close to the true value), reliability (consistent results), precision "
            "(how close repeated readings are to each other) and replication (whether others get the same result).",
            "Hypothesis: a thicker bracket won't crack under vibration. Test three thicknesses on a vibration rig, "
            "repeat each test, and compare with the prediction.",
            [("What is a hypothesis?", "A testable explanation."),
             ("What is precision?", "How close repeated readings are to each other."),
             ("Why repeat tests?", "To check results are reliable.")]),
        "Measurement equipment": E(
            "Choose measuring equipment by the accuracy you need.\n\n"
            "A steel rule measures to about 0.5 mm. Vernier and digital callipers measure inside, outside and depth "
            "dimensions to about 0.02 mm. Micrometers measure small diameters and thicknesses to 0.01 mm or better. "
            "Dial test indicators show small variations such as run-out. Coordinate measuring machines (CMMs) measure "
            "complex 3D shapes to microns.\n\n"
            "Key principles: resolution (the smallest change it can show), accuracy, precision, uncertainty, "
            "calibration against a known standard, and tolerance.",
            "Checking a 12 mm shaft toleranced to plus or minus 0.01 mm needs a micrometer: a calliper isn't precise enough.",
            [("Which tool measures small diameters most precisely?", "A micrometer."),
             ("What is resolution?", "The smallest change an instrument can show."),
             ("Why calibrate instruments?", "So readings match a known standard.")]),
    },
    "core/07-forces-motion-and-energy.pptx": {
        "Motion and moments": E(
            "Motion can be rotary (turning), linear (in a straight line), reciprocating (back and forth in a line) "
            "or oscillating (swinging back and forth in an arc).\n\n"
            "A moment is the turning effect of a force: moment = force x perpendicular distance from the pivot, "
            "measured in newton metres. Torque is the turning effect about an axis, such as on a bolt or shaft.\n\n"
            "An object is in equilibrium when the forces balance and the clockwise moments equal the anticlockwise "
            "moments. Engineers use this to find unknown forces.",
            "A 40 N force on a spanner 0.25 m from the bolt gives 40 x 0.25 = 10 N m of torque. A longer spanner "
            "gives more torque for the same force.",
            [("What is the formula for a moment?", "Force x perpendicular distance."),
             ("What motion does a piston make?", "Reciprocating."),
             ("What is equilibrium?", "Forces balance and clockwise moments equal anticlockwise moments.")]),
        "Newton's laws of motion": E(
            "Newton's first law: an object stays at rest, or keeps moving at a constant velocity, unless a resultant "
            "(unbalanced) force acts on it.\n\n"
            "Newton's second law: force = mass x acceleration (F = ma). A bigger force, or a smaller mass, gives a "
            "bigger acceleration.\n\n"
            "Newton's third law: when one object pushes on another, the second pushes back with an equal and opposite force.\n\n"
            "These laws explain everything from a car braking to a rocket launching.",
            "A 1,200 kg car accelerating at 2 m/s squared needs a resultant force of 1,200 x 2 = 2,400 N.",
            [("State Newton's second law as a formula.", "F = ma."),
             ("What force accelerates 50 kg at 3 m/s squared?", "150 N."),
             ("Which law explains recoil when firing?", "Newton's third law.")]),
        "Simply supported beams": E(
            "A simply supported beam rests on two supports and carries loads.\n\n"
            "To find the support reactions, take moments about one support: the moment of the load about that "
            "support equals the moment of the other reaction about it. Then the reactions must add up to the total load.\n\n"
            "Shear force diagrams show the internal sliding forces along the beam; bending moment diagrams show "
            "where it bends most. The maximum bending moment tells designers where the beam is most likely to fail.",
            "A 6 m beam with 3 kN at 2 m from the left support: right reaction = 3 x 2 / 6 = 1 kN; left reaction = "
            "3 - 1 = 2 kN.",
            [("How do you find a support reaction?", "Take moments about the other support."),
             ("What must the reactions add up to?", "The total load."),
             ("What does a bending moment diagram show?", "Where and how much the beam bends.")]),
        "Energy and power": E(
            "Work done = force x distance moved, in joules. Power = work done / time, in watts.\n\n"
            "Kinetic energy (energy of movement) = half x mass x velocity squared. Potential energy (energy of "
            "height) = mass x g x height, where g is 9.81 m/s squared.\n\n"
            "Energy is conserved: it changes form but isn't lost, although some becomes heat through friction. "
            "Momentum (mass x velocity) is conserved in collisions.\n\n"
            "Power sources include mechanical, electrical and renewable (solar, hydro, wind, geothermal), plus fossil "
            "fuels and nuclear.",
            "Lifting a 50 kg load 2 m gains 50 x 9.81 x 2 = 981 J of potential energy. Doing it in 5 s takes about 196 W.",
            [("What is the kinetic energy of 2 kg moving at 4 m/s?", "16 J."),
             ("A motor does 1,200 J in 20 s. What is its power?", "60 W."),
             ("What is the formula for potential energy?", "mgh.")]),
    },
    "core/08-fluid-dynamics-and-thermodynamics.pptx": {
        "Fluids at rest and in motion": E(
            "Hydrostatic pressure increases with depth: pressure = density x g x depth. That's why dams are thicker "
            "at the bottom.\n\n"
            "Viscosity is a fluid's resistance to flowing: oil is more viscous than water.\n\n"
            "Bernoulli's principle says that where a fluid speeds up, its pressure drops. It explains how "
            "carburettors and aircraft wings work.\n\n"
            "Flow can be laminar (smooth, orderly layers) or turbulent (chaotic, swirling). Turbulence, vortices and "
            "separation points, where flow leaves a surface, increase drag.",
            "At 10 m depth in water, extra pressure = 1,000 x 9.81 x 10 = 98,100 Pa, nearly one extra atmosphere.",
            [("What happens to pressure with depth?", "It increases."),
             ("State Bernoulli's principle.", "Where a fluid speeds up, its pressure drops."),
             ("What is viscosity?", "A fluid's resistance to flow.")]),
        "Heat": E(
            "Heat moves by conduction (through solids, particle to particle), convection (by moving fluids, such as "
            "warm air rising) and radiation (by electromagnetic waves, needing no medium).\n\n"
            "Sensible heat changes an object's temperature. Latent heat changes its state, such as ice melting, "
            "without changing temperature.\n\n"
            "Materials expand when heated (expansivity), so engineers leave gaps in bridges and rails.\n\n"
            "Systems are closed (no mass enters or leaves) or open (mass flows through, like an engine).",
            "A heatsink uses conduction to draw heat from a chip, then convection (a fan) to carry it away into the air.",
            [("Which heat transfer needs no medium?", "Radiation."),
             ("What does latent heat do?", "Changes state without changing temperature."),
             ("Why do bridges have expansion gaps?", "Materials expand when heated.")]),
        "The gas laws": E(
            "The gas laws link the pressure (p), volume (V) and temperature (T) of a gas. Temperature must be in "
            "kelvin: K = degrees C + 273.\n\n"
            "Boyle's law, at constant temperature: p1 V1 = p2 V2. Squash a gas and its pressure rises.\n\n"
            "Charles' law, at constant pressure: V1 / T1 = V2 / T2. Heat a gas and it expands.\n\n"
            "The general gas equation combines them: p1 V1 / T1 = p2 V2 / T2. The characteristic gas equation, "
            "pV = mRT, links them to the mass of gas and its gas constant R.",
            "A gas at 100 kPa and 4 litres is compressed to 1 litre at constant temperature: p2 = 100 x 4 / 1 = 400 kPa.",
            [("What units must temperature be in?", "Kelvin."),
             ("Which law applies at constant temperature?", "Boyle's law."),
             ("Convert 50 degrees C to kelvin.", "323 K.")]),
    },
    "core/09-materials-chemistry-properties-and-structures.pptx": {
        "Chemistry for engineers": E(
            "Atoms have a nucleus of protons and neutrons, surrounded by electrons. The outer (valence) electrons "
            "form bonds, which give materials their properties.\n\n"
            "Metallic bonds share a 'sea' of electrons, making metals conduct and bend. Covalent bonds share "
            "electrons between atoms, giving strong, often brittle materials. Ionic bonds transfer electrons between "
            "atoms. Weak van der Waals forces hold polymer chains together.\n\n"
            "Chemistry also matters for cells and batteries, electrolysis (used in plating) and how metals react "
            "with acids and alkalis, which is used in etching and surface finishing.",
            "Copper conducts electricity well because its metallic bonding lets electrons move freely.",
            [("Which particles form bonds?", "Valence (outer) electrons."),
             ("Why do metals conduct electricity?", "Metallic bonding lets electrons move freely."),
             ("What is electrolysis used for in engineering?", "E.g. electroplating.")]),
        "Properties of materials": E(
            "Physical properties describe how a material behaves without being loaded: density, melting point, "
            "thermal and electrical conductivity, expansivity, corrosion resistance, weldability and recyclability.\n\n"
            "Mechanical properties describe how it responds to force. Strength resists breaking under tension, "
            "compression, shear or torsion. Hardness resists scratching and wear. Toughness absorbs impact without "
            "breaking; brittleness is the opposite. Ductility lets it be drawn into wire; malleability lets it be "
            "hammered into shape. Elasticity means it returns to shape; plasticity means it stays deformed.\n\n"
            "Density = mass / volume.",
            "Glass is hard but brittle: it resists scratches but shatters on impact. Rubber is tough and elastic.",
            [("What is the difference between hardness and toughness?", "Hardness resists scratching; toughness resists breaking on impact."),
             ("A 5.4 kg block is 0.002 cubic metres. What is its density?", "2,700 kg per cubic metre."),
             ("What is ductility?", "The ability to be drawn into wire.")]),
        "Families of materials": E(
            "Ferrous metals contain iron, such as steels and cast iron. They're strong but most rust. Non-ferrous "
            "metals, such as aluminium, copper and brass, don't rust and are often lighter.\n\n"
            "Thermoplastics, such as ABS and acrylic, soften when heated and can be reshaped and recycled. Thermosets, "
            "such as epoxy resin, set permanently when cured. Elastomers, such as rubber, stretch and return.\n\n"
            "Composites combine materials: glass or carbon fibre in resin gives strength with low weight. Ceramics "
            "are hard and heat-resistant but brittle.",
            "A bike frame might be steel (ferrous, cheap), aluminium (non-ferrous, light) or carbon fibre composite "
            "(very light, expensive).",
            [("What is a ferrous metal?", "One containing iron."),
             ("What is the difference between thermoplastics and thermosets?", "Thermoplastics can be reshaped when heated; thermosets set permanently."),
             ("Why use composites?", "High strength with low weight.")]),
    },
    "core/10-processing-treatment-failure-and-testing.pptx": {
        "Heat and surface treatments": E(
            "Heat treatments change a metal's structure and properties.\n\n"
            "Quench hardening heats steel and cools it rapidly, making it very hard but brittle; tempering then "
            "reheats it gently to reduce brittleness. Case hardening gives a hard outer skin with a tough core. "
            "Annealing softens metal and relieves stress; normalising refines its grain. Precipitation hardening "
            "strengthens some alloys, such as aluminium.\n\n"
            "Surface treatments protect against corrosion: painting and plastic coating form a barrier; galvanising "
            "coats steel with zinc, which corrodes first to protect it.\n\n"
            "Processing, such as rolling, forging and welding, also changes properties.",
            "A chisel is quench hardened so its edge stays sharp, then tempered so it doesn't shatter when hit with a hammer.",
            [("Why temper after quench hardening?", "To reduce brittleness."),
             ("What does annealing do?", "Softens the metal and relieves stress."),
             ("How does galvanising protect steel?", "The zinc coating corrodes first.")]),
        "Why materials fail": E(
            "Corrosion is chemical attack, such as rust, that removes material and can eventually perforate it. It "
            "includes oxidation, chemical attack and stress corrosion.\n\n"
            "Fatigue is failure under repeated loading, even when each load is well below the breaking stress: tiny "
            "cracks grow with every cycle until the part snaps.\n\n"
            "Creep is slow, permanent deformation under a constant load, especially at high temperature. It happens "
            "in three stages: primary, secondary (steady) and tertiary, ending in fracture.\n\n"
            "Prevention includes coatings, galvanising, sacrificial anodes and designing out stress concentrations.",
            "Bending a paperclip back and forth until it snaps is fatigue: no single bend breaks it, but the "
            "repeated cycles do.",
            [("What is fatigue?", "Failure from repeated loading below the breaking stress."),
             ("When is creep a concern?", "Under constant load, especially at high temperature."),
             ("What is a sacrificial anode?", "A more reactive metal that corrodes instead of the protected part.")]),
        "Tensile testing": E(
            "A tensile test stretches a sample until it breaks, recording the load and extension.\n\n"
            "Stress = force / cross-sectional area. Strain = extension / original length (no units). In the elastic "
            "region, extension is proportional to load (Hooke's law) and the sample returns to shape. Young's modulus "
            "= stress / strain in this region, a measure of stiffness.\n\n"
            "Beyond the elastic limit it deforms plastically. The ultimate tensile strength is the maximum stress; "
            "after that the sample narrows (necks) and fractures.\n\n"
            "Other tests include hardness, impact (toughness), fatigue (Wohler), wear and corrosion.",
            "A 10 kN load on a 50 square millimetre bar gives a stress of 10,000 / 0.00005 = 200 MPa.",
            [("What is the formula for stress?", "Force / area."),
             ("What does Young's modulus measure?", "Stiffness (stress / strain)."),
             ("What is necking?", "The sample narrowing before it fractures.")]),
    },
    "core/11-electrical-and-electronic-principles.pptx": {
        "Key quantities": E(
            "Current (I) is the flow of charge, measured in amps. Voltage (V) is the push that drives it, in volts. "
            "Resistance (R) opposes the flow, in ohms. Power (P) is the rate energy is used, in watts.\n\n"
            "Ohm's law: V = I x R. Power: P = V x I.\n\n"
            "Other key ideas: capacitance (storing charge), inductance (opposing changes in current), magnetism and "
            "electromagnetism (used in motors and relays), and measuring these quantities with a multimeter.",
            "A 12 V supply across a 4 ohm resistor gives I = 12 / 4 = 3 A, and P = 12 x 3 = 36 W.",
            [("State Ohm's law.", "V = I x R."),
             ("What is the unit of resistance?", "The ohm."),
             ("A device draws 2 A at 230 V. What is its power?", "460 W.")]),
        "Series and parallel": E(
            "In a series circuit, components are in one loop. The same current flows through each, the voltages "
            "across them add up to the supply voltage, and total resistance = R1 + R2 + ... If one component fails, "
            "the whole circuit stops.\n\n"
            "In a parallel circuit, each component has its own branch. Each gets the full supply voltage, the "
            "branch currents add up to the total, and 1 / R total = 1 / R1 + 1 / R2 + ... One failure doesn't stop the others.\n\n"
            "Kirchhoff's laws: current into a junction equals current out; voltages around a loop sum to zero.",
            "Two 10 ohm resistors: in series, 20 ohms; in parallel, 5 ohms. Household sockets are wired in parallel.",
            [("In series, what is the same through every component?", "The current."),
             ("Two 6 ohm resistors in parallel give what total?", "3 ohms."),
             ("Why are house circuits in parallel?", "Each device gets full voltage and works independently.")]),
        "Signals": E(
            "An analogue signal varies continuously, like the voltage from a temperature sensor rising smoothly as it "
            "warms. It carries fine detail but is easily affected by noise.\n\n"
            "A digital signal has discrete levels, usually just on (1) and off (0), like a limit switch. It resists "
            "noise and is easy for computers and PLCs to process.\n\n"
            "Analogue-to-digital converters turn sensor readings into numbers. Fan-in and fan-out limit how many "
            "inputs and outputs a logic gate can connect to. Signals often need conditioning (filtering or amplifying).",
            "A car's fuel gauge sender produces an analogue voltage; the engine computer converts it to a digital "
            "value to display.",
            [("What is an analogue signal?", "One that varies continuously."),
             ("Give one advantage of digital signals.", "E.g. resist noise, easy to process."),
             ("What does an ADC do?", "Converts analogue signals to digital.")]),
    },
    "core/12-mechatronics.pptx": {
        "Components of a mechatronic system": E(
            "Mechatronics combines mechanical and electronic systems into one.\n\n"
            "Mechanical components, such as gears, cams, linkages, levers and pulleys, transmit and change motion. "
            "Electronic components sense and control: sensors and transducers measure things, microprocessors and "
            "microcontrollers decide what to do, and actuators make things move.\n\n"
            "Drives provide the motion: standard electric motors for continuous rotation, servo motors for precise "
            "positions using feedback, and stepper motors that move in fixed steps without needing feedback.",
            "A 3D printer: stepper motors move the head precisely, a microcontroller runs the program, and a "
            "thermistor senses the nozzle temperature.",
            [("What does an actuator do?", "Creates movement."),
             ("Which motor uses feedback for precise positioning?", "A servo motor."),
             ("What does a transducer do?", "Converts one form of energy or signal into another.")]),
        "Programmable logic controllers (PLCs)": E(
            "A PLC is a rugged industrial computer that controls machines and processes.\n\n"
            "Unitary PLCs are compact all-in-one units; modular PLCs are built from plug-in modules, so inputs and "
            "outputs can be added as needed.\n\n"
            "A PLC conditions signals from sensors, runs its program (often ladder logic), and drives outputs such as "
            "motors and valves through driver circuits and interfaces.\n\n"
            "PLCs run robotic arms, conveyors, packaging lines and SCADA systems. They're more rugged and easier to "
            "reprogram than dedicated circuits, but cost more than a simple circuit.",
            "On a bottling line, a sensor detects each bottle; the PLC counts them and tells the capper to fire at "
            "exactly the right moment.",
            [("What is the difference between unitary and modular PLCs?", "Unitary is all-in-one; modular is built from plug-in modules."),
             ("Give two applications of PLCs.", "E.g. robotic arms, conveyors, packaging."),
             ("Why use a PLC rather than a dedicated circuit?", "Rugged and easy to reprogram.")]),
        "Hydraulics and pneumatics": E(
            "Both use fluid under pressure to transmit power.\n\n"
            "Hydraulics uses oil, which is almost incompressible. It produces very large forces with precise control, "
            "but leaks are messy and the oil can be a fire risk. It's used in excavators and presses.\n\n"
            "Pneumatics uses compressed air, which is springy (compressible). It's fast, clean and cheap, but gives "
            "lower forces and less precise positioning. It's used in pick-and-place machines and bus doors.\n\n"
            "Components include pumps and compressors, valves, cylinders and actuators, shown with standard symbols "
            "on schematic diagrams.",
            "A car crusher uses hydraulics for its huge force; a factory sorting line uses pneumatic cylinders to "
            "push small parts quickly.",
            [("Which system uses nearly incompressible fluid?", "Hydraulics."),
             ("Give one advantage of pneumatics.", "E.g. fast, clean, cheap."),
             ("Why is pneumatic positioning less precise?", "Air is compressible.")]),
    },
    "core/13-control-systems.pptx": {
        "Parts of a control system": E(
            "Every control system has inputs, processes and outputs.\n\n"
            "Inputs are sensors measuring pressure, flow, temperature, speed or position. Processes decide what to "
            "do, using logic gates (AND, OR, NOT), timers, comparators, counters and latches. Outputs act on the "
            "world: motors, valves, heaters and lamps.\n\n"
            "Feedback sends information about the output back to the input, so the system can correct itself. A "
            "summing point compares the desired value (set point) with the actual value.",
            "A safety guard: the machine runs only if the guard sensor AND the start button are both on, an AND gate.",
            [("Name three process blocks.", "E.g. logic gates, timers, counters, comparators, latches."),
             ("What is feedback?", "Information about the output sent back to the input."),
             ("What does an AND gate need to output 1?", "Both inputs to be 1.")]),
        "Open and closed loop": E(
            "An open loop system has no feedback: it runs a set action regardless of the result. It's simple and "
            "cheap but can't correct errors, like a toaster on a timer.\n\n"
            "A closed loop system measures its output and feeds it back to compare with the set point, correcting "
            "any difference automatically, like an oven thermostat or cruise control.\n\n"
            "Closed loop systems can be under-damped (overshooting and oscillating) or over-damped (slow to reach the "
            "set point). Steady-state error is any difference that remains once the system settles.",
            "Cruise control set to 70 mph: going uphill the car slows, the sensor detects it, and the controller adds power.",
            [("What does an open loop system lack?", "Feedback."),
             ("What is an under-damped system?", "One that overshoots and oscillates."),
             ("What is steady-state error?", "The difference left between set point and output once settled.")]),
        "Sensors and actuators in automation": E(
            "Sensors can be analogue (a continuous range, like temperature) or digital (on or off, like a limit "
            "switch). Active sensors need power; passive ones don't.\n\n"
            "Common examples are switches, proximity sensors (detecting objects without contact), lasers and vision "
            "systems (cameras that inspect or guide).\n\n"
            "Connections can be hard-wired, which is reliable, or wireless, which is flexible.\n\n"
            "In automation they position and measure objects and control lifting and moving, measuring electrical, "
            "mechanical, thermal, chemical, optical and acoustic quantities.",
            "A vision system photographs every biscuit on a conveyor and signals an actuator to reject any that are broken.",
            [("What is a proximity sensor?", "A sensor that detects objects without contact."),
             ("What is the difference between active and passive sensors?", "Active sensors need power; passive ones don't."),
             ("Give one use of a vision system.", "E.g. inspecting products for defects.")]),
    },
    "core/14-quality-management.pptx": {
        "Quality assurance and quality control": E(
            "Quality assurance (QA) prevents defects by building quality into the process: a quality culture, "
            "'right first time', traceability, document and version control, and standards such as ISO 9001.\n\n"
            "Quality control (QC) finds defects by inspecting and testing products against the specification.\n\n"
            "Statistical process control (SPC) samples production and plots measurements on charts, spotting drift "
            "before parts go out of tolerance. It's faster and cheaper than inspecting every item in high volumes. "
            "Process capability shows whether a process can consistently meet its tolerance.",
            "An SPC chart shows shaft diameters creeping upwards as a tool wears. The tool is changed before any "
            "shaft goes out of tolerance.",
            [("Is inspection QA or QC?", "QC."),
             ("What does SPC do?", "Samples production to spot drift before defects occur."),
             ("What is 'right first time'?", "Getting it correct without rework.")]),
        "Improving quality": E(
            "Six sigma uses data to reduce variation, aiming for almost no defects in high-volume production. Total "
            "quality management (TQM) makes everyone responsible for quality.\n\n"
            "FMEA (Failure Mode and Effects Analysis) lists how things could fail and how serious each would be, so "
            "the worst are designed out. Pareto analysis shows that most problems usually come from a few causes. "
            "Cause and effect (fishbone) diagrams trace problems to root causes. Quality circles are small teams of "
            "workers who meet to solve quality problems.",
            "A Pareto chart shows 80% of rejects come from two causes: loose fixings and scratches. Fixing those two "
            "solves most of the problem.",
            [("What does a Pareto chart show?", "Which few causes create most problems."),
             ("What is a quality circle?", "A small team of workers solving quality problems."),
             ("What does six sigma aim to reduce?", "Variation and defects.")]),
        "Standard operating procedures": E(
            "A standard operating procedure (SOP) is a written, step-by-step instruction for doing a task the same "
            "way every time.\n\n"
            "Types include manufacturing, quality and maintenance SOPs. They standardise work, keep customers "
            "satisfied with consistent products, keep people safe and support training.\n\n"
            "An SOP typically includes a title, purpose, scope, responsibilities, equipment, the method step by step, "
            "safety notes and a revision history. SOPs are written, put into use, evaluated and updated under "
            "version control.",
            "An SOP for setting up a lathe means every operator fits the guard, checks the chuck key is removed and "
            "sets the speed the same way.",
            [("What is an SOP?", "A written step-by-step procedure for doing a task consistently."),
             ("Give two purposes of SOPs.", "E.g. consistency, safety, training, customer satisfaction."),
             ("Why include a revision history?", "To show which version is current and what changed.")]),
    },
    "core/15-health-and-safety-legislation.pptx": {
        "Key legislation": E(
            "The Health and Safety at Work Act (HASAWA) sets general duties for everyone at work. The Management "
            "Regulations require risk assessments. PUWER makes sure work equipment is safe and maintained. LOLER "
            "covers lifting operations and equipment. The PPE Regulations cover protective equipment. The Noise at "
            "Work Regulations protect hearing. The Manual Handling and Work at Height Regulations cover lifting and "
            "working above ground. The Electricity at Work Regulations cover electrical safety. CEMFAW covers first "
            "aid. RIDDOR requires serious incidents to be reported. COSHH controls hazardous substances.",
            "Using an overhead crane brings in LOLER (the crane), PUWER (the equipment), PPE (hard hats) and HASAWA (general duty).",
            [("Which regulations cover lifting equipment?", "LOLER."),
             ("What does COSHH control?", "Hazardous substances."),
             ("What does RIDDOR require?", "Reporting serious injuries, diseases and dangerous occurrences.")]),
        "Responsibilities": E(
            "Employees must work safely, not attempt tasks they're not trained or authorised for, co-operate with "
            "their employer, and never interfere with or misuse safety equipment.\n\n"
            "Employers must minimise risks from handling, storage and transport, provide instruction, training and "
            "supervision, maintain a safe workplace, publish a health and safety policy, arrange safety "
            "representatives and committees, and protect visitors, contractors and the public.\n\n"
            "The Health and Safety Executive (HSE) enforces the law. Breaking it can mean injury, prosecution, fines "
            "and damaged reputations.",
            "A worker removes a machine guard to work faster and is injured. Both the worker (misusing safety "
            "equipment) and the employer (supervision) may be at fault.",
            [("Name two employee responsibilities.", "E.g. work safely, co-operate, don't misuse safety equipment."),
             ("Who enforces health and safety law?", "The HSE."),
             ("Must employers protect visitors?", "Yes.")]),
    },
    "core/16-risk-assessment-and-hazardous-contexts.pptx": {
        "Stages of risk assessment": E(
            "Risk assessment has three core stages.\n\n"
            "Identify hazards: anything that could cause harm, such as machinery, stored energy, tools, electricity, "
            "harmful substances and the environment. Methods include HAZOP (a structured study of a process) and "
            "HAZID (hazard identification workshops).\n\n"
            "Evaluate the risk: how likely harm is, how severe it would be and how many people could be affected.\n\n"
            "Implement control measures using the hierarchy of control, then record and review them.",
            "A pressurised air receiver: hazard (stored energy), risk (explosion injuring several people), control "
            "(pressure relief valve, regular inspection, guarding).",
            [("What is a hazard?", "Anything that could cause harm."),
             ("Name the three factors in evaluating risk.", "Likelihood, severity and number of people affected."),
             ("What is HAZOP?", "A structured study of a process to find hazards.")]),
        "The hierarchy of control": E(
            "Controls are chosen from the top of the hierarchy down, because higher controls are more effective.\n\n"
            "Eliminate the hazard completely. Reduce it or substitute something less hazardous. Isolate people from "
            "it. Use engineering controls such as guards, interlocks and extraction. Use administrative controls: "
            "training, safe systems of work, permits and signs. Finally, provide PPE such as eye and ear protection, "
            "safety shoes, gauntlets and helmets.\n\n"
            "PPE is the last resort because it only protects the wearer and depends on being worn correctly.",
            "Noisy machine: replace it with a quieter one (substitute), enclose it (engineering), limit exposure time "
            "(administrative), then provide ear defenders (PPE).",
            [("What is the top level of the hierarchy?", "Elimination."),
             ("Give an example of an engineering control.", "E.g. guards, interlocks, extraction."),
             ("Why is PPE the last resort?", "It only protects the wearer and relies on correct use.")]),
        "Specific engineering contexts": E(
            "Some work needs extra precautions.\n\n"
            "Moving parts need guarding and isolation. Lock out tag out (LOTO) means switching off and physically "
            "locking energy sources before work, so nobody can restart the machine. Confined spaces risk suffocation "
            "and need oxygen checks, a permit to work and a rescue plan. Chemicals need COSHH assessments, "
            "ventilation and fire precautions. Electrical testing and high-voltage work need safe isolation, permits "
            "and competent people, and awareness of stored energy.",
            "Before clearing a jam in a conveyor, the fitter isolates the power, fits their own padlock and tag, and "
            "tests that it won't start.",
            [("What is LOTO?", "Locking and tagging energy sources off before work."),
             ("What is a permit to work?", "Written authorisation with conditions for high-risk work."),
             ("Why are confined spaces dangerous?", "E.g. lack of oxygen, toxic gases, difficult escape.")]),
    },
    "core/17-environmental-legislation.pptx": {
        "Environmental legislation": E(
            "Engineering can harm the environment, so several laws apply.\n\n"
            "The Environmental Protection Act sets a duty of care for waste and controls pollution. The Pollution "
            "Prevention and Control Act requires permits for polluting industrial activity. The Clean Air Act "
            "controls smoke and air pollution. The Radioactive Substances Act controls radioactive materials. The "
            "Controlled Waste, Hazardous Waste and Dangerous Substances rules govern handling, storage and disposal.\n\n"
            "Everyone shares responsibility for compliance, led by management.",
            "Used cutting fluid is hazardous waste: it must be stored safely and collected by a licensed carrier, "
            "with records kept.",
            [("Which Act sets a duty of care for waste?", "The Environmental Protection Act."),
             ("Which Act controls smoke?", "The Clean Air Act."),
             ("How must hazardous waste be removed?", "By a licensed carrier, with records.")]),
        "ISO 14001": E(
            "ISO 14001 is the international standard for environmental management systems.\n\n"
            "It helps an organisation identify its environmental impacts, set targets to reduce them, comply with "
            "the law and keep improving.\n\n"
            "Benefits include lower costs through using less energy and producing less waste, easier legal "
            "compliance, and a better reputation, which helps win contracts.\n\n"
            "Ignoring environmental responsibilities risks fines, prosecution, lost contracts and environmental damage.",
            "A factory certified to ISO 14001 cuts its energy bills by 15% after monitoring shows compressors running "
            "all night unnecessarily.",
            [("What does ISO 14001 cover?", "Environmental management systems."),
             ("Give two benefits.", "E.g. lower costs, compliance, reputation."),
             ("Give one consequence of ignoring environmental law.", "E.g. fines, prosecution, lost contracts.")]),
    },
    "core/18-business-commercial-and-financial-awareness.pptx": {
        "Commercial operations": E(
            "Businesses aim to make a profit while meeting stakeholders' needs.\n\n"
            "Efficiency matters: value-added activities, such as machining a part, make the product worth more; "
            "non-value-added activities, such as moving parts around or waiting, cost money without adding value.\n\n"
            "Markets can be local, national or international. Prices are shaped by supply, demand and competition, "
            "and activities are judged on quality, cost and time. Research and development (R&D) and innovation keep "
            "products competitive.",
            "Cutting the time parts spend waiting between machines from 2 days to 2 hours adds no cost but frees "
            "cash and space: removing non-value-added activity.",
            [("What is a value-added activity?", "One that makes the product worth more."),
             ("Give an example of non-value-added activity.", "E.g. waiting, unnecessary transport."),
             ("Why invest in R&D?", "To stay competitive through innovation.")]),
        "Financial concepts": E(
            "Direct costs are tied to each product, such as materials. Indirect costs and overheads keep the "
            "business running, such as rent and electricity.\n\n"
            "Break-even is the number of units where revenue equals total costs. Above it, the business makes a profit.\n\n"
            "Cash flow is money moving in and out over time. Even a profitable business can fail if cash runs out "
            "before customers pay. Creditors are people you owe; debtors owe you.\n\n"
            "Assets lose value over time (depreciation). Finance comes from loans, shares or capital.",
            "Fixed costs 6,000 pounds a month; each part sells for 10 pounds and costs 4 pounds to make. Break-even = "
            "6,000 / 6 = 1,000 parts a month.",
            [("What is break-even?", "Where revenue equals total costs."),
             ("Is rent a direct or indirect cost?", "Indirect."),
             ("Why can a profitable business run out of cash?", "Money may go out before customers pay.")]),
    },
    "core/19-professional-conduct-cpd-and-human-factors.pptx": {
        "CPD and professional recognition": E(
            "Continuous professional development (CPD) is ongoing learning throughout your career: training "
            "courses, industry placements, academic study, events and seminars.\n\n"
            "CPD keeps skills current, motivates staff and improves performance.\n\n"
            "The Engineering Council sets the professional standards for engineers in the UK. With experience and "
            "evidence of competence, engineers can register as an Engineering Technician (EngTech), Incorporated "
            "Engineer (IEng) or Chartered Engineer (CEng), recognised by employers worldwide.",
            "A T Level student might become an apprentice, gain EngTech registration, then study part-time towards IEng or CEng.",
            [("What is CPD?", "Ongoing professional learning throughout a career."),
             ("Who sets professional standards for UK engineers?", "The Engineering Council."),
             ("Name one professional registration level.", "EngTech, IEng or CEng.")]),
        "Human factors": E(
            "Human factors are the ways people's physical and mental abilities and limits affect work.\n\n"
            "Workplace design affects safety, comfort and productivity: badly placed controls, poor lighting or "
            "awkward postures cause mistakes and injuries.\n\n"
            "Human error is often caused by insufficient training, fatigue, heavy workload and stress. It's reduced "
            "by good training, sensible shift patterns, clear procedures, well-designed workplaces and error-proofing "
            "(designs that make mistakes impossible).",
            "A connector that only fits one way round (error-proofing) prevents the mistake entirely, which is better "
            "than a warning in the manual.",
            [("Name two causes of human error.", "E.g. training, fatigue, workload, stress."),
             ("What is error-proofing?", "Designing so mistakes are impossible."),
             ("How does workplace design affect safety?", "Poor layout, lighting or posture cause mistakes and injuries.")]),
    },
    "core/20-stock-and-asset-management.pptx": {
        "Stock practices": E(
            "Just-in-time (JIT) delivers parts exactly when they're needed, keeping stock low and freeing cash, but "
            "any supply disruption stops production.\n\n"
            "Made-to-stock builds products to a forecast and holds them ready, giving fast delivery but risking "
            "unsold or obsolete stock.\n\n"
            "Made-to-order builds only when a customer orders, with no unsold stock but longer lead times.\n\n"
            "Material requirements planning (MRP) calculates exactly what materials are needed and when, from the "
            "production schedule. It depends on accurate data.",
            "A car plant using JIT keeps only hours of parts on site. When a supplier's factory flooded, the whole "
            "line stopped within a day.",
            [("What is the main risk of JIT?", "Supply disruption stops production."),
             ("When is made-to-order best?", "For customised or low-volume products."),
             ("What does MRP calculate?", "What materials are needed and when.")]),
        "Asset life cycle": E(
            "Assets such as machines are managed through four stages: plan what's needed, acquire it, operate and "
            "maintain it, then dispose of it by selling, recycling or scrapping.\n\n"
            "Whole-life budgeting considers the total cost over the asset's life, not just the purchase price, "
            "including maintenance, energy and disposal. Depreciation records the loss of value over time.\n\n"
            "Capacity management, such as manufacturing resource planning, finds bottlenecks: the stage that limits "
            "the whole process's output.",
            "A cheaper machine that uses twice the energy and needs more servicing can cost more over ten years than "
            "a pricier efficient one.",
            [("Name the four asset life cycle stages.", "Plan, acquire, operate and maintain, dispose."),
             ("What is a bottleneck?", "The stage that limits the whole process's output."),
             ("Why use whole-life costing?", "The purchase price isn't the total cost.")]),
    },
    "core/21-continuous-improvement.pptx": {
        "The PDCA cycle": E(
            "Continuous improvement means making small, steady improvements all the time, known as Kaizen.\n\n"
            "The PDCA cycle structures it. Plan: identify a problem and plan a change. Do: try it on a small scale. "
            "Check: measure the results against key performance indicators (KPIs). Act: adopt it if it worked, adjust "
            "it, or abandon it, then start again.\n\n"
            "KPIs, such as scrap rate, output per hour or on-time delivery, show whether things are really improving. "
            "Lean thinking focuses on removing waste.",
            "Plan: rearrange a workbench to cut walking. Do: trial it for a week. Check: assembly time falls 12%. "
            "Act: roll it out to all benches.",
            [("What does PDCA stand for?", "Plan, do, check, act."),
             ("What is Kaizen?", "Continuous small improvements by everyone."),
             ("Why use KPIs?", "To measure whether changes really improve things.")]),
        "The 8 wastes": E(
            "Lean identifies eight wastes that add cost but no value.\n\n"
            "Transportation: moving materials unnecessarily. Inventory: holding too much stock. Motion: people moving "
            "more than needed. Waiting: idle time. Over-production: making more than is needed. Over-processing: "
            "doing more work than the customer requires. Defects: scrap and rework. Unused talent: not using people's "
            "skills and ideas.\n\n"
            "Practices such as value stream mapping, 6S, SMED, OEE, TPM and kanban help remove them.",
            "Polishing a hidden internal surface the customer never sees is over-processing: it costs time and adds no value.",
            [("Name four of the 8 wastes.", "Any four of the eight."),
             ("What is over-processing?", "Doing more than the customer requires."),
             ("Why is unused talent a waste?", "People's skills and ideas aren't being used.")]),
        "Improvement practices": E(
            "Value stream mapping draws every step of a process to find waste. Visual management and kanban make "
            "status and demand visible at a glance.\n\n"
            "6S organises the workplace: sort, set in order, shine, standardise, sustain and safety.\n\n"
            "SMED (single minute exchange of dies) cuts changeover times so small batches become practical.\n\n"
            "OEE (overall equipment effectiveness) = availability x performance x quality, showing how well a machine "
            "is really used. TPM (total productive maintenance) has operators help maintain their own machines.",
            "A press is available 90% of the time, runs at 80% speed and makes 95% good parts: OEE = 0.9 x 0.8 x 0.95 "
            "= about 68%.",
            [("What is the OEE formula?", "Availability x performance x quality."),
             ("What does SMED reduce?", "Changeover time."),
             ("Name the six parts of 6S.", "Sort, set in order, shine, standardise, sustain, safety.")]),
    },
    "core/22-project-management.pptx": {
        "The project life cycle": E(
            "Projects follow a life cycle. Initiation sets the brief, goals and success criteria. Planning works out "
            "resources, schedule and risks. Implementation does the work. Monitoring tracks progress against the "
            "plan. Reporting keeps stakeholders informed. Evaluation reviews what went well and what to improve.\n\n"
            "Constraints include budget, cost, quality, time, safety, resources, communication, reputation and "
            "changing requirements. Risks are managed throughout.\n\n"
            "Collaborative working, including matrix structures and shared digital tools, helps teams work together.",
            "Designing a new jig: the brief sets the target cycle time, the plan schedules design, manufacture and "
            "testing, and the evaluation records lessons for the next jig.",
            [("What happens at initiation?", "The brief, goals and success criteria are set."),
             ("Name three project constraints.", "E.g. budget, time, quality."),
             ("Why evaluate a finished project?", "To learn lessons for future projects.")]),
        "Planning and control": E(
            "Planning starts by identifying the resources needed: time, budget, people, training, communication and "
            "production facilities.\n\n"
            "A Gantt chart shows tasks as bars on a timeline. Critical path analysis (CPA) finds the longest chain of "
            "dependent tasks, which sets the shortest possible project length. PERT uses optimistic, likely and "
            "pessimistic estimates. Contingency plans prepare for things going wrong.\n\n"
            "Control uses monitoring reports on budget, quality, cost and time. Managing by stages approves each stage "
            "before the next; managing by exception escalates only when agreed limits are exceeded.",
            "Tasks: design 3 days, order parts 5, machine 4, assemble 2, test 1. If ordering can start during design, "
            "the critical path is order, machine, assemble, test: 12 days.",
            [("What does the critical path determine?", "The shortest possible project length."),
             ("What is managing by exception?", "Escalating only when limits are exceeded."),
             ("What does PERT use?", "Optimistic, likely and pessimistic time estimates.")]),
    },
    "core/23-employer-set-project.pptx": {
        "What is the ESP?": E(
            "The Employer-set Project is worth 30% of the core and has 18.5 hours of assessment time. City & Guilds "
            "sets and marks it.\n\n"
            "It's a realistic, complex industry brief developed with employers, and it draws on knowledge from across "
            "the whole engineering core, plus maths, English and digital skills. It's linked to four core skills: "
            "planning and preparation, communication, develop and manufacture, and evaluation.\n\n"
            "Specialism knowledge isn't assessed here; it's covered separately in the practical assignment.",
            "A brief might ask for a solution to a real manufacturing problem, such as redesigning a component to "
            "cut cost while meeting safety standards.",
            [("What percentage of the core is the ESP?", "30%."),
             ("Who sets and marks the ESP?", "City & Guilds."),
             ("Name two of the four core skills.", "Any two: planning and preparation, communication, develop and manufacture, evaluation.")]),
        "Assessment objectives": E(
            "The ESP is marked against five assessment objectives.\n\n"
            "AO1 (13%): plan your approach, showing it is planned, sequenced, prioritised and iterative. AO2 (50%): "
            "apply core knowledge and skills to the brief. AO3 (13%): select and use relevant techniques and "
            "resources accurately. AO4 (10%): use maths, English and digital skills correctly, with the right terms, "
            "units and calculations. AO5 (13%): realise the outcome and review how well it meets the brief, including "
            "why other options were rejected.\n\n"
            "Half the marks come from AO2, so link your knowledge explicitly to the brief.",
            "Instead of 'I chose aluminium', write 'I chose aluminium because its density (2,700 kg per cubic metre) "
            "keeps weight low and it resists corrosion in damp conditions'.",
            [("Which AO carries half the marks?", "AO2."),
             ("What does AO4 assess?", "Maths, English and digital skills."),
             ("Why explain rejected options?", "AO5 rewards evaluating other options considered.")]),
    },
}
