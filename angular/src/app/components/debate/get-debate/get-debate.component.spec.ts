import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GetDebateComponent } from './get-debate.component';

describe('GetDebateComponent', () => {
  let component: GetDebateComponent;
  let fixture: ComponentFixture<GetDebateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GetDebateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GetDebateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
