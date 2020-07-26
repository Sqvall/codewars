const ipToInt32 = (ip) => (ip.split('.').reduce((a, v) => ((a << 8) + (+v)), 0) >>> 0);

console.log(ipToInt32("128.32.10.1")); // return: 2149583361
