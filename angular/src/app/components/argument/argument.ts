export class Argument {
    constructor(
        public title: string,
        public content: string,
        public user_id: string,
        public debate_id: string
    ) {
        this.title = title;
        this.content = content;
        this.user_id = user_id;
        this.debate_id = debate_id;
    }
}
