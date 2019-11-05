import { Argument } from 'src/app/components/argument/argument';

export class Debate {
    constructor(
        public title: string,
        public description: string,
        public content: string,
        public creator_id: string,
        public community_id: string,
        public arg_list: Argument[]
    ) {
    }
}
