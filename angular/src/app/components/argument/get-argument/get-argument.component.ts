import { Component, Input } from '@angular/core';
import { ArgumentService } from 'src/app/services/argument/argument.service';

import { ActivatedRoute, Router } from '@angular/router';

import { Argument } from '../argument';

@Component({
  selector: 'app-argument',
  templateUrl: './get-argument.component.html',
  styleUrls: ['./get-argument.component.css']
})
export class GetArgumentComponent {
  private argument: Argument;

  constructor(
    private service: ArgumentService,
    private router: Router
    ) {
  }

  @Input()
  set argument_id(argument_id: number) {
    console.log('here');
    this.service.getArgument(String(argument_id))
    .subscribe(
      argument => {
        this.argument = argument;
        console.log(argument);
      },
      error => {
        console.log(error);
        this.router.navigate(['404']);
      });
  }
}
