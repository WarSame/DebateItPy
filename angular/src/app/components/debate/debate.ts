import { Argument } from 'src/app/components/argument/argument';

export class Debate {
    constructor(
        public title: string,
        public description: string,
        public creator_id: string,
        public community_id: string,
        public arg_ids: number[]
    ) {
    }
}
