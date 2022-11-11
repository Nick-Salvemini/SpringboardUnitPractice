beforeAll(() => {
    console.log('Before All')
});

beforeEach(() => {
    console.log('Before Each')
})

describe('calculate taxes test', function () {
    it('should calculate the high tax bracket', function () {
        // expect(1 + 1).toEqual(2);
        expect(calculateTaxes(50000)).toEqual(12500);
        expect(calculateTaxes(100000)).toEqual(25000);
    })

    it('should calculate the low tax bracket', function () {
        // expect(2 + 1).toEqual(2);
        expect(calculateTaxes(10000)).toEqual(1500);
        expect(calculateTaxes(1000)).toEqual(150);
        expect(calculateTaxes(0)).toEqual(0);
    })

    it('should reject invalid incomes', function () {
        expect(() => calculateTaxes('asdfasdf')).toThrowError();
        expect(() => calculateTaxes([])).toThrowError();
        expect(() => calculateTaxes(true)).toThrowError();
    })
})

describe('remove duplicates test', function () {
    it('should remove duplicates from an array', function () {
        expect(removeDupes([1, 1, 2, 2, 3, 3, 4, 4])).toEqual([1, 2, 3, 4]);
        expect(removeDupes([1, 2, 3, 4])).toEqual([1, 2, 3, 4]);
        expect(removeDupes([1, 2, 3, 4])).toBeInstanceOf(Array);
    })

    it('should remove duplicates from a string', function () {
        expect(removeDupes('hello')).toBe('helo');
        expect(removeDupes('pie')).toBe('pie');
        expect(removeDupes('hello')).toBeInstanceOf(String);
    })
})

describe('remove values from array test', function () {
    it('should remove value from array', function () {
        expect(remove([1, 2, 3, 4], 4)).not.toContain(4);
    })
})

describe('submit form test', function () {
    it('should add username to the array', function () {
        nameInput.value = 'nick';
        submitForm();
        expect(usernames.length).toBe(1)
        expect(usernames).toContain('nick');
    })
})

afterEach(function () {
    nameInput.value = '';
    usernames = [];
})

afterAll(() => {
    console.log('After All')
});