// Variables
var f1 = 5.6;
var f2 = 4.3;
var f3 = 3.6;
var f4 = 2.8;
var f5 = 4.1;

var totalForce = f1 + f2 + f3 + f4 + f5;
console.log("Force = " + totalForce);

// Lists
var fs = [5.6, 4.3, 3.6, 2.8, 4.1];
var totalForce = 0;
for (var i = 0; i <fs.length; i++) {
    totalForce += fs[i];
}

console.log("Force = " + totalForce);

// If statements
var totalForce = 100;
var capacity = 90;

if (totalForce > capacity) {
    console.log("Force exceeds capacity");
}
else if (Math.abs(totalForce - capacity) < 1.0E-6) {
    console.log("Force equals capacity");
}
else {
    console.log("Force is within capacity");
}

// Functions
function checkAginstCapacity(total, capacity) {
    if (total > capacity) {
        return "Force exceeds capacity";
    }
    else if (abs(total - capacity) < 1.0E-6) {
        return "Force equals capacity";
    }
    else {
        return "Force is within capacity";
    }
}

console.log("Force" + checkAginstCapacity(totalForce, capacity));

// Objects
class Force {
    constructor(x, y, z) {
    this.X = x;
    this.Y = y;
    this.Z = z;
    }

    tostring() {
        return this.X + ", " + this.Y + ", " + this.Z;
    }
    }
  var f = new Force(-0.3, 0.0, 5.6);
  
  var fs = [new Force(-0.3, 0.0, 5.6),
            new Force(1.2, 0.0, 4.3),
            new Force(0.0, 0.0, 3.6),
            new Force(0.5, 0.0, 2.8),
            new Force(-1.0, 0.0, 4.1)];

var totalForce = new Force(0.0, 0.0, 0.0);
for (var i = 0; i < fs.length; i++) {
    totalForce.X += fs[i].X;
    totalForce.Y += fs[i].Y;
    totalForce.Z += fs[i].Z;
}
var totalForce = new Force(0.0, 0.0, 0.0);
fs.forEach((f) => {
    totalForce.X += f.X;
    totalForce.Y += f.Y;
    totalForce.Z += f.Z;
})

console.log("totalForce = " + totalForce.tostring())
