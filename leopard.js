this.stage.vars.t = 0;
    while (true) {
      yield* this.render(this.stage.vars.t);
      this.stage.vars.t++;
      yield;
    }