export class Post {
    constructor(
        public title: string,
        public text: string,
        public user_id: string,
        public debate_id: string
    ) {
        this.title = title;
        this.text = text;
        this.user_id = user_id;
        this.debate_id = debate_id;
    }
}
