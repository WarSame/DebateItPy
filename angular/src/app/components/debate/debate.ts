import { Post } from 'src/app/components/post/post';

export class Debate {
    constructor(
        public title: string,
        public description: string,
        public text: string,
        public creator_id: string,
        public community_id: string,
        public posts: Post[]
    ) {
    }
}
