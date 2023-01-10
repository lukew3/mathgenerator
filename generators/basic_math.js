function randint(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}

export function absolute_difference(max_a=100, max_b=100) {
    const a = randint(-1 * max_a, max_a);
    const b = randint(-1 * max_b, max_b);
    const absDiff = Math.abs(a - b);
    return [`$|${a}-${b}|$`, `$${absDiff}$`];
}

export function addition(max_sum=99, max_addend=50) {
    if (max_addend > max_sum) max_addend = max_sum;
    const a = randint(0, max_addend);
    const b = randint(0, max_addend);
    const c = a + b;
    const problem = `$${a}+${b}=$`;
    const solution = `$${c}$`;

    return [problem, solution]
}

export function compare_fractions(max_val=10) {
    const a = randint(1, max_val);
    let b = randint(1, max_val);
    const c = randint(1, max_val);
    let d = randint(1, max_val);

    while (a == b) b = randint(1, max_val);
    while (c == d) d = randint(1, max_val);

    const first = a / b;
    const second = c / d;

    let solution;
    if (first > second) {
        solution = '>';
    } else if (first < second) {
        solution = '<';
    } else {
        solution = '=';
    }

    const problem = `Which symbol represents the comparison between $\\frac{${a}}{${b}}$ and $\\frac{${c}}{${d}}$?`;
    return [problem, solution];
}

export function cube_root(min_no=1, max_no=1000) {
    const a = randint(min_no, max_no);
    const b = a ** (1 / 3);

    return [`$\\sqrt[3]{${a}}=$`, `$${b}$`];
}

export function divide_fractions(max_val=10) {
    const a = randint(1, max_val);
    let b = randint(1, max_val);
    while (a == b) b = randint(1, max_val);

    const c = randint(1, max_val);
    let d = randint(1, max_val);
    while (c == d) d = randint(1, max_val);

    function calculate_gcd(x, y) {
        while (y) {
            var t = y;
            y = x % y;
            x = t;
        }
        return x;
    }

    const tmp_n = a * d;
    const tmp_d = b * c;
    
    const gcd = calculate_gcd(tmp_n, tmp_d);
    const sol_numerator = Math.floor(tmp_n / gcd);
    const sol_denominator = Math.floor(tmp_d / gcd);

    return [`$\\frac{${a}}{${b}}\\div\\frac{${c}}{${d}}=$`, `$\\frac{${sol_numerator}}{${sol_denominator}}$`];
}
