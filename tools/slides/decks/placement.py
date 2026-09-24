"""
Where each deck's inline link goes on each page.

Maps deck file -> {page: [targets]}. A target is either:
  - a specification number such as "6.2", matched against the number (or
    number range) at the start of a page's ## or ### heading;
  - "top", placing the link after the page's introduction (for a deck that
    covers the whole page);
  - any other string, matched against the start of a heading's text.

The link goes at the end of the section's text. If a deck's sections are not
next to each other on the page, the link appears after each group.
"""

P1 = "01-core-component/01-engineering-core-part1.md"
P2 = "01-core-component/02-engineering-core-part2.md"
ESP = "01-core-component/03-employer-set-project.md"
KNOW = "02-occupational-specialism/01-knowledge-criteria.md"
PRAC = "02-occupational-specialism/02-practical-criteria.md"

PLACEMENT = {
    "core/01-design-principles-and-manufacturing-approaches.pptx": {P1: ["1.1", "1.3"]},
    "core/02-maintenance-repair-and-installation.pptx": {P1: ["1.2"]},
    "core/03-engineering-past-present-and-future.pptx": {P1: ["2.1", "2.2", "2.3"]},
    "core/04-engineering-drawings-and-tolerancing.pptx": {P1: ["3.1", "3.2"]},
    "core/05-essential-mathematics.pptx": {P1: ["4.1", "4.2"]},
    "core/06-units-measurement-and-scientific-method.pptx": {P1: ["5.1", "5.2", "5.3", "5.4"]},
    "core/07-forces-motion-and-energy.pptx": {P1: ["5.6", "7.1", "7.2"]},
    "core/08-fluid-dynamics-and-thermodynamics.pptx": {P1: ["5.7", "5.8"]},
    "core/09-materials-chemistry-properties-and-structures.pptx": {P1: ["5.5", "6.1", "6.2"]},
    "core/10-processing-treatment-failure-and-testing.pptx": {P1: ["6.3", "6.4", "6.5", "6.6"]},
    "core/11-electrical-and-electronic-principles.pptx": {P1: ["8.1"]},
    "core/12-mechatronics.pptx": {P2: ["9.1", "9.2", "9.3"]},
    "core/13-control-systems.pptx": {P2: ["10.1", "10.2"]},
    "core/14-quality-management.pptx": {P2: ["11.1", "11.2"]},
    "core/15-health-and-safety-legislation.pptx": {P2: ["12.1", "12.2", "12.3"], KNOW: ["1.14"]},
    "core/16-risk-assessment-and-hazardous-contexts.pptx": {P2: ["12.4", "12.5"]},
    "core/17-environmental-legislation.pptx": {P2: ["12.6"]},
    "core/18-business-commercial-and-financial-awareness.pptx": {P2: ["13.1", "13.2", "13.3"]},
    "core/19-professional-conduct-cpd-and-human-factors.pptx": {P2: ["14.1", "14.2", "14.3"]},
    "core/20-stock-and-asset-management.pptx": {P2: ["15.1", "15.2"]},
    "core/21-continuous-improvement.pptx": {P2: ["16.1"]},
    "core/22-project-management.pptx": {P2: ["17.1", "17.2", "17.3"]},
    "core/23-employer-set-project.pptx": {ESP: ["top"]},
    "specialism/01-design-principles-methodologies-and-verification.pptx": {KNOW: ["1.1", "1.2", "1.8"]},
    "specialism/02-mechanical-drawings-standards-and-communication.pptx": {KNOW: ["1.3", "1.4", "1.20"]},
    "specialism/03-simple-machines-and-mechanical-calculations.pptx": {KNOW: ["1.5", "1.6", "1.13"]},
    "specialism/04-loads-environment-and-aerodynamics.pptx": {KNOW: ["1.7", "1.12"]},
    "specialism/05-business-context-constraints-and-metrics.pptx": {KNOW: ["1.9"]},
    "specialism/06-materials-standard-parts-and-processes.pptx": {KNOW: ["1.10", "1.11"]},
    "specialism/07-quality-testing-and-measurement.pptx": {KNOW: ["1.15", "1.17", "1.18", "1.19"]},
    "specialism/08-installation-and-integration.pptx": {KNOW: ["1.16"]},
    "specialism/09-analysing-requirements-and-design-information.pptx": {PRAC: ["Outcome 2"]},
    "specialism/10-evaluating-and-improving-designs.pptx": {PRAC: ["Outcome 3"]},
    "specialism/11-designing-modelling-and-prototyping.pptx": {PRAC: ["Outcome 4"]},
    "specialism/12-collaboration-risk-and-quality-assurance.pptx": {PRAC: ["Outcome 5"]},
    "specialism/13-technical-documentation-and-communication.pptx": {PRAC: ["Outcome 6"]},
}
