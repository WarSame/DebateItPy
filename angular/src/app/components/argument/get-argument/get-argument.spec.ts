import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GetArgumentComponent } from './get-argument.component';

describe('ArgumentComponent', () => {
  let component: GetArgumentComponent;
  let fixture: ComponentFixture<GetArgumentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GetArgumentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GetArgumentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
