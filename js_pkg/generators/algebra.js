import {randint, randomchoice, calculate_gcd, intParser} from '../utils.js';

export function basic_algebra(max_variable=10) {
    const a = randint(1, max_variable);
    const b = randint(1, max_variable);
    const c = randint(1, max_variable);

    const i = calculate_gcd(a, b);
    let x = `${Math.floor((c - b) / i)}/${Math.floor(a / i)}`;

    if (c - b == 0) {
        x = "0";
    } else if (a == 1 || a == i) {
        x = `${c - b}`;
    }

    return [`$${a}x + ${b} = ${c}$`, `$${x}$`];
}

export function combine_like_terms(max_coef=10, max_exp=20, max_terms=10) {
    const numTerms = randint(1, max_terms);
    let coefs = [];
    for (let i = 0; i < numTerms; i++) {
        coefs.push(randint(1, max_coef));
    }
    let exponents = [];
    for (let i = 0; i < numTerms; i++) {
        exponents.push(randint(1, Math.max(max_exp - 1, 2)));
    }
    let terms = [];
    for (let i = 0; i < numTerms; i++) {
        terms.push(`${coefs[i]}x^{${exponents[i]}}`);
    }
    const problem = terms.join(" + ");
    let d = {};
    for (let i = 0; i < numTerms; i++) {
        if (d.hasOwnProperty(exponents[i])) {
            d[exponents[i]] += coefs[i];
        } else {
            d[exponents[i]] = coefs[i];
        }
    }
    d.sort();
    const termsSol = [];
    for (let i = 0; i < numTerms; i++) {
        termsSol += `${d[k]}x^{${k}}`
    }
    const solution = termsSol.join(' + ');
    return [`$${problem}$`, `$${solution}$`]
}

export function complex_quadratic(prob_type=0, max_range=10) {
    // TODO: Implement
}

export function compound_interest(max_principle=10000, max_rate=10, max_time=10) {
    const p = randint(1000, max_principle);
    const r = randint(1, max_rate);
    const n = randint(1, max_time);
    const a = Math.round(p * Math.pow(1 + r / 100, n), 2);
    const problem = `Compound interest for a principle amount of $${p}$ dollars, $${r}$% rate of interest and for a time period of $${n}$ years is $=$`;
    return [problem, `$${a}$`];
}

export function distance_two_points(max_val_xy=20, min_val_xy=-20) {
    const point1X = randint(min_val_xy, max_val_xy + 1);
    const point1Y = randint(min_val_xy, max_val_xy + 1);
    const point2X = randint(min_val_xy, max_val_xy + 1);
    const point2Y = randint(min_val_xy, max_val_xy + 1);

    const distanceSq = Math.pow(point1X - point2X, 2) + Math.pow(point1Y - point2Y, 2);
    const problem = `Find the distance between $(${point1X}, ${point1Y})$ and $(${point2X}, ${point2Y})$`;
    return [problem, `$\\sqrt{${distanceSq}}`];
}

export function expanding(range_x1=10, range_x2=10, range_a=10, range_b=10) {
    // TODO: Implement
}

export function factoring(range_x1=10, range_x2=10) {
    let x1 = randint(-range_x1, range_x1);
    let x2 = randint(-range_x1, range_x2);
    let b = intParser(x1 + x2);
    const c = intParser(x1 * x2);

    if (b == '+1') {
        b = '+';
    }
    if (b == '') {
        problem = `x^2${c}`;
    } else {
        problem = `x^2${b}x${c}`
    }

    const x1s = intParser(x1);
    const x2s = intParser(x2);
    return [`$${problem}$`, `$(x${x1s})(x${x2s})$`];
}
