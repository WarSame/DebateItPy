import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent implements OnInit {

  constructor(private http:HttpClient) { }

  ngOnInit() {
    let test = this.http.get("http://localhost:80/test").subscribe(
        data => console.log(data),
        error => console.log(error),
        () => console.log("done")
    );
  }

}
