function calculateTaxes(income) {
    // if (!Number.isFinite(income)) {
    //     throw new Error('Invalid Income');
    // }
    if (!Number.isFinite(income)) {
        throw new Error('BAD INCOME');
    }
    if (income > 30000) {
        return income * .25;
    }
    else {
        return income * .15;
    }
}

console.log(calculateTaxes(500));

function removeDupes(values) {
    const arr = [...new Set(values)];

    if (typeof values === 'string') {
        return arr.join('');
    }
    return arr
}

function remove(arr, val) {
    return arr.filter((el) => {
        return el !== val
    })
}

let usernames = [];
let nameInput = document.querySelector('#username');
function submitForm() {
    usernames.push(nameInput.value);
}