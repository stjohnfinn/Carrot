// Get current score (by ABC)
let _rScore = "0";
CanvasRenderingContext2D.prototype.fillText = new Proxy(CanvasRenderingContext2D.prototype.fillText, {
    apply(fillRect, ctx, [text, x, y, ...blah]) {

        if (text.startsWith('Score: ')) _rScore = text

        console.log(_rScore)

        fillRect.call(ctx, text, x, y, ...blah);
    }
})