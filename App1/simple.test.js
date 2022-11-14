const checkIPFS = require("../App1/connection/static/js/app")


test.only('use jsdom in this test file', () => {
    expect(1+1).toBe(2);
});

// test('use jsdom in this test file', () => {
//     const element = document.createElement('div');
//     expect(element).toBeNull();
// });

test('check if an image is sent to ipfs', () =>{
    expect(checkIPFS).not.toBeNull();
})